import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect('ecommerce.db')

# SQL Query: Total revenue by product
query = """
SELECT p.name AS product_name, 
       SUM(oi.quantity * p.price) AS total_revenue
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
GROUP BY p.name;
"""

# Run query and get results
df = pd.read_sql(query, conn)

# Save to Excel
df.to_excel("sales_report.xlsx", index=False)

print("✅ Report generated: sales_report.xlsx")
conn.close()