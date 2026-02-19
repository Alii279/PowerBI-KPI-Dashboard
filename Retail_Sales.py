"""
Python Code to generate synthetic dataset to be published in retail_sales_synthetic_dataset.csv
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

# -----------------------------
# Configuration
# -----------------------------
num_records = 20000
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)

regions = ["West", "Central", "East", "Atlantic"]
segments = ["Consumer", "Corporate", "Home Office"]
categories = {
    "Technology": ["Phones", "Accessories", "Copiers", "Machines"],
    "Furniture": ["Chairs", "Tables", "Bookcases", "Furnishings"],
    "Office Supplies": ["Binders", "Paper", "Storage", "Art"]
}


# -----------------------------
# Helper Functions
# -----------------------------

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))


def generate_sales(category):
    base = {
        "Technology": np.random.normal(400, 150),
        "Furniture": np.random.normal(300, 120),
        "Office Supplies": np.random.normal(150, 60)
    }
    return max(10, round(base[category], 2))


def generate_discount(segment):
    if segment == "Corporate":
        return round(np.random.uniform(0.05, 0.25), 2)
    return round(np.random.uniform(0.0, 0.2), 2)


# -----------------------------
# Generate Data
# -----------------------------

data = []

for i in range(num_records):
    category = random.choice(list(categories.keys()))
    sub_category = random.choice(categories[category])
    segment = random.choice(segments)
    region = random.choice(regions)

    order_date = random_date(start_date, end_date)
    ship_date = order_date + timedelta(days=random.randint(1, 7))

    sales = generate_sales(category)
    discount = generate_discount(segment)
    profit = round(sales * (0.15 - discount), 2)

    data.append([
        f"ORD-{100000 + i}",
        f"CUST-{random.randint(1000, 3000)}",
        order_date,
        ship_date,
        region,
        segment,
        category,
        sub_category,
        sales,
        discount,
        profit
    ])

columns = [
    "Order_ID",
    "Customer_ID",
    "Order_Date",
    "Ship_Date",
    "Region",
    "Segment",
    "Category",
    "Sub_Category",
    "Sales",
    "Discount",
    "Profit"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("retail_sales_synthetic_dataset.csv", index=False)

df.head()
