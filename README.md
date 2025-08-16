# E-Commerce Sales Reporting System

This is a beginner-friendly project that creates a simple SQL-based reporting system for an e-commerce store.

## 🔧 Features
- SQL schema with `customers`, `products`, `orders`, and `order_items`
- Python script to generate revenue reports from SQL queries
- Exports data to Excel using `pandas`

## 🛠 Tech Stack
- SQLite
- Python (sqlite3, pandas, openpyxl)


## 🚀 Project Overview

This project simulates a mini e-commerce analytics system that integrates database design, SQL queries, and Python-based reporting.
It demonstrates the end-to-end data workflow — from setting up a relational database to extracting insights and generating an automated sales report.

The final output is an Excel report (sales_report.xlsx) that shows total revenue per product.
## 🗂️ Project Structure
├── init_db.py        # Script to create and populate the database
├── report.py         # Script to generate sales report
├── schema.sql        # Database schema (tables)
├── seed_data.sql     # Sample data for customers, products, and orders
├── ecommerce.db      # SQLite database (auto-created when running init_db.py)
├── sales_report.xlsx # Generated Excel report (output)
└── README.md         # Project documentation

## ⚙️ Setup Instructions

Clone the repository

git clone https://github.com/your-username/ecommerce-analytics.git
cd ecommerce-analytics


Install dependencies
Make sure you have Python 3 installed. Then install required libraries:

pip install pandas openpyxl


Initialize the database

python init_db.py


This will create ecommerce.db using schema.sql and populate it with seed_data.sql.

Generate the sales report

python report.py


The script will create sales_report.xlsx containing revenue by product.

🛠️ How It Works

Database Creation (init_db.py)

Connects to SQLite and runs schema.sql to define tables:

customers, products, orders, order_items

Loads sample records from seed_data.sql

Data Analysis (report.py)

Runs an SQL query:

SELECT p.name AS product_name, 
       SUM(oi.quantity * p.price) AS total_revenue
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
GROUP BY p.name;


Fetches results with Pandas

Saves the report into Excel (sales_report.xlsx)

## 📈 Example Output

sales_report.xlsx

product_name	total_revenue
Laptop	      800.00
Headphones	   300.00
## 🎯 Results

Successfully built an end-to-end data pipeline for e-commerce analytics.

Automated generation of Excel sales reports for revenue insights.

## 🧰 Skills & Tools Demonstrated

SQL: Schema design, joins, aggregations

SQLite: Lightweight relational database

Python: Database connectivity and automation

Pandas: Data extraction, transformation, and export

Excel (openpyxl): Business-friendly reporting

## 📌 Use Cases

Business Intelligence reporting

Sales performance analysis

Learning project for SQL + Python integration

