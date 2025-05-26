import pandas as pd
import uuid
from faker import Faker
from random import randint, uniform

fake = Faker()
data = []

for _ in range(1000):  # generate 1000 fake records
    data.append({
        "sale_id": str(uuid.uuid4()),
        "timestamp": fake.date_time_between(start_date='-30d', end_date='now'),
        "product_id": f"P{randint(100,999)}",
        "region": fake.random_element(["North", "South", "East", "West"]),
        "sale_amount": round(uniform(500, 5000), 2)
    })

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)
print("Dummy sales data generated!")
