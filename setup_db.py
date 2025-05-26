import pandas as pd
import sqlite3

# Step 1: Read your CSV
df = pd.read_csv("sales_data.csv")

# Step 2: Create a SQLite DB file (or connect if already exists)
conn = sqlite3.connect("sales.db")  # This creates a new file named sales.db

# Step 3: Load the DataFrame into a new table called "sales"
df.to_sql("sales", conn, if_exists="replace", index=False)

# Step 4: Close the connection
conn.commit()
conn.close()

print("✅ Data loaded into SQLite database (sales.db)")
