
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- Create synthetic 100-row dataset ---
np.random.seed(42)
products = [
    {"Product": "Classic Notebook", "Category": "Stationery", "UnitPrice": 149.0},
    {"Product": "Gel Pen Pack (5)", "Category": "Stationery", "UnitPrice": 99.0},
    {"Product": "Desk Organizer", "Category": "Office", "UnitPrice": 499.0},
    {"Product": "Wireless Mouse", "Category": "Electronics", "UnitPrice": 799.0},
    {"Product": "USB-C Cable", "Category": "Electronics", "UnitPrice": 249.0},
    {"Product": "Bluetooth Speaker", "Category": "Electronics", "UnitPrice": 2199.0},
    {"Product": "Ceramic Coffee Mug", "Category": "Home & Kitchen", "UnitPrice": 299.0},
    {"Product": "Stainless Water Bottle", "Category": "Home & Kitchen", "UnitPrice": 699.0},
    {"Product": "Yoga Mat", "Category": "Sports", "UnitPrice": 1199.0},
    {"Product": "Resistance Bands", "Category": "Sports", "UnitPrice": 599.0},
    {"Product": "Cotton T-Shirt", "Category": "Apparel", "UnitPrice": 449.0},
    {"Product": "Denim Jeans", "Category": "Apparel", "UnitPrice": 1599.0},
    {"Product": "LED Desk Lamp", "Category": "Home & Kitchen", "UnitPrice": 1299.0},
    {"Product": "Portable Power Bank", "Category": "Electronics", "UnitPrice": 1499.0},
    {"Product": "Phone Case", "Category": "Electronics", "UnitPrice": 349.0},
    {"Product": "Notebook Stand", "Category": "Office", "UnitPrice": 999.0},
    {"Product": "Backpack", "Category": "Apparel", "UnitPrice": 1999.0},
    {"Product": "Scented Candle", "Category": "Home & Kitchen", "UnitPrice": 399.0},
    {"Product": "Running Shoes", "Category": "Apparel", "UnitPrice": 2999.0},
    {"Product": "Wireless Earbuds", "Category": "Electronics", "UnitPrice": 3499.0},
]
catalog = pd.DataFrame(products)

num_rows = 100
num_orders = np.random.randint(60, 81)
order_ids = [f"ORD-{1000+i}" for i in range(num_orders)]
assigned_orders = np.random.choice(order_ids, size=num_rows, replace=True)

start_date = datetime(2025, 9, 1)
end_date = datetime(2025, 12, 1)

def random_date(start, end, n):
    delta_days = (end - start).days
    return [start + timedelta(days=int(x)) for x in np.random.randint(0, delta_days + 1, size=n)]

order_dates_map = dict(zip(order_ids, random_date(start_date, end_date, len(order_ids))))
num_customers = 45
customer_ids = [f"CUST-{2000+i}" for i in range(num_customers)]
order_customer_map = dict(zip(order_ids, np.random.choice(customer_ids, size=len(order_ids), replace=True)))
channels = ["Online", "Retail Store", "Marketplace"]
payments = ["Card", "UPI", "COD", "NetBanking"]
order_channel_map = dict(zip(order_ids, np.random.choice(channels, size=len(order_ids), replace=True)))
order_payment_map = dict(zip(order_ids, np.random.choice(payments, size=len(order_ids), replace=True)))

rows = []
for i in range(num_rows):
    prod = catalog.sample(1, replace=True).iloc[0]
    qty = int(np.random.choice([1,1,1,2,2,3,3,4,5]))
    unit_price = round(float(prod.UnitPrice) * np.random.uniform(0.9, 1.1), 2)
    line_total = round(unit_price * qty, 2)
    oid = assigned_orders[i]
    rows.append({
        "OrderID": oid,
        "OrderDate": order_dates_map[oid].date().isoformat(),
        "CustomerID": order_customer_map[oid],
        "Channel": order_channel_map[oid],
        "PaymentMethod": order_payment_map[oid],
        "Product": prod.Product,
        "Category": prod.Category,
        "UnitPrice": unit_price,
        "Quantity": qty,
        "LineTotal": line_total,
    })

df = pd.DataFrame(rows)

# --- Build the Category vs Month pivot ---
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)

pivot = pd.pivot_table(
    df,
    index="Category",
    columns="Month",
    values="LineTotal",
    aggfunc="sum",
    fill_value=0
)
pivot = pivot.reindex(sorted(pivot.columns), axis=1)

# --- Save both data and pivot into one workbook ---
out_path = "retail_100_rows_with_pivot.xlsx"
with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Data")
    pivot.to_excel(writer, sheet_name="Pivot_Category_vs_Month")

print("Saved:", out_path)
print("Pivot shape:", pivot.shape)
print("Pivot preview:", pivot.head())
