import sqlite3
import pandas as pd

# 1. Connect to your SQLite DB
conn = sqlite3.connect("sales.db")

# 2. Read the full “sales” table
df = pd.read_sql("SELECT * FROM sales", conn)

# 3. Write out a fresh CSV for Power BI
df.to_csv("sales_output.csv", index=False)

conn.close()
print("✅ sales_output.csv updated from sales.db")
