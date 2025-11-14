import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Create customer table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    location TEXT
);
""")

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product TEXT,
    quantity INTEGER,
    price REAL,
    date TEXT
);
""")

conn.commit()
conn.close()

print("Database and tables created successfully!")
