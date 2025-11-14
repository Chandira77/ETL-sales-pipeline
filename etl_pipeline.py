import pandas as pd
import sqlite3

# 1. EXTRACT
customers = pd.read_csv("customers.csv")
sales = pd.read_csv("sales.csv")

# 2. TRANSFORM
# Remove duplicates
customers = customers.drop_duplicates()
sales = sales.drop_duplicates()

# Add total amount column
sales["total_amount"] = sales["quantity"] * sales["price"]

# Convert date to correct format
sales["date"] = pd.to_datetime(sales["date"])

# Join both tables
merged_data = sales.merge(customers, on="customer_id", how="left")

# 3. LOAD
conn = sqlite3.connect("sales.db")

# Load into database
customers.to_sql("customers", conn, if_exists="replace", index=False)
sales.to_sql("sales", conn, if_exists="replace", index=False)
merged_data.to_sql("sales_report", conn, if_exists="replace", index=False)

conn.close()

print("ETL Pipeline completed successfully!")
