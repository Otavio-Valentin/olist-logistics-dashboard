import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="Olist Logistics Dashboard", layout="wide")

# --- 1. Load Data (REAL DATA MERGE) ---
@st.cache_data
def load_data():
    # 1. Read files separately
    df_orders = pd.read_csv("data/olist_orders_dataset.csv")
    df_items = pd.read_csv("data/olist_order_items_dataset.csv")
    df_customers = pd.read_csv("data/olist_customers_dataset.csv")
    
    # 2. Merge Orders with Items (using 'order_id')
    df_temp = pd.merge(df_orders, df_items, on="order_id")
    
    # 3. Merge result with Customers (using 'customer_id')
    # Now we have: Dates, Freight, and State in the same table
    df_final = pd.merge(df_temp, df_customers, on="customer_id")
    
    return df_final

df = load_data()

# --- 2. Sidebar (Filters) ---
st.sidebar.header("Logistics Filters")
selected_state = st.sidebar.multiselect(
    "Filter by State:",
    options=df["customer_state"].unique(),
    default=df["customer_state"].unique()
)

# Apply Filter
df_selection = df.query("customer_state == @selected_state")

# --- 3. Main KPIs ---
st.title("🚚 Logistics Dashboard - Olist")
st.markdown("---")

col1, col2, col3 = st.columns(3)

total_orders = df_selection.shape[0]
# Using Mean (.mean) as market standard, but .sum() can be used for totals
avg_freight = df_selection["freight_value"].mean() 
delivery_rate = (df_selection[df_selection["order_status"] == "delivered"].shape[0] / total_orders) * 100 if total_orders > 0 else 0

with col1:
    st.metric(label="Total Orders", value=total_orders)
with col2:
    st.metric(label="Average Freight Cost ($)", value=f"{avg_freight:.2f}")
with col3:
    st.metric(label="Delivery Rate", value=f"{delivery_rate:.1f}%")

st.markdown("---")

# --- 4. Charts ---
col_graph1, col_graph2 = st.columns(2)

with col_graph1:
    st.subheader("Top 10 States by Freight Cost")
    
    # 1. Group data by State and Sum Freight value
    df_grouped = df_selection.groupby("customer_state")["freight_value"].sum().reset_index()
    
    # 2. Sort from Highest to Lowest and keep only Top 10
    df_grouped = df_grouped.sort_values(by="freight_value", ascending=False).head(10)
    
    # 3. Create chart with summarized data
    fig_bar = px.bar(df_grouped, x="customer_state", y="freight_value", 
                     title="Top 10 States (Freight)", 
                     template="plotly_white",
                     text_auto='.2s') # Shows value on top of the bar
    st.plotly_chart(fig_bar, use_container_width=True)

with col_graph2:
    st.subheader("Order Status Distribution")
    
    # 1. Count orders by status (Aggregation)
    df_status_counts = df_selection["order_status"].value_counts().reset_index()
    df_status_counts.columns = ["order_status", "count"]
    
    # 2. Create Donut Chart
    fig_pie = px.pie(df_status_counts, values="count", names="order_status", 
                     title="Order Status",
                     hole=0.5, # Creates the hole in the middle (Donut)
                     template="plotly_white")
    
    # 3. Configure to show legend and percentages
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)