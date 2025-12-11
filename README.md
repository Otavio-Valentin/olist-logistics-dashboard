# 🚚 Olist Logistics Performance Dashboard

## 📊 Project Overview
This project is a **Business Intelligence (BI)** web application built with Python to analyze the logistics performance of Olist, the largest department store marketplace in Brazil.
The tool processes over **112,000 real order records**, enabling the identification of delivery bottlenecks and freight cost efficiency in real-time.

**Goal:** To demonstrate how to replace slow Excel-based analysis with scalable Python dashboards.

---

## 🛠️ Tech Stack
| Technology | Purpose |
| :--- | :--- |
| **Python** | Core business logic and data processing. |
| **Pandas** | ETL (Extract, Transform, Load) and complex **Data Merging** of multiple CSV files. |
| **Streamlit** | Framework for building and deploying the interactive web dashboard. |
| **Plotly Express** | Dynamic data visualization and KPI monitoring. |

---

## 📂 Data Source
Due to performance reasons and GitHub file size limits, the raw CSV files are not hosted in this repository.
This project uses the **Brazilian E-Commerce Public Dataset by Olist**, publicly available on Kaggle.

👉 **[Click here to download the dataset on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)**

**Required file structure in the root folder:**
* `olist_orders_dataset.csv`
* `olist_order_items_dataset.csv`
* `olist_customers_dataset.csv`

*(Note: These files must be downloaded and placed in the project directory manually before running the app).*

---

## 🚀 How to Run Locally

Follow these steps to clone and run the dashboard on your machine:

**Prerequisites:** Python 3.8+ and Git installed.

**1. Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/olist-logistics-dashboard.git](https://github.com/YOUR_USERNAME/olist-logistics-dashboard.git)

2. Install required libraries:

Bash

pip install streamlit pandas plotly
3. Run the Dashboard:

Bash

streamlit run dashboard.py
