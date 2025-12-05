
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

CUSTOMERS_CSV = "customers.csv"
ORDERS_CSV = "orders.csv"

def create_customers(n_customers: int = 50, seed: int = 123) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    first_names = ["Aarav", "Isha", "Rohan", "Anaya", "Vihaan", "Siya", "Arjun", "Mira", "Ishaan", "Anika",
                   "Kabir", "Kiara", "Advait", "Sara", "Reyansh", "Aditi", "Vivaan", "Riya", "Dhruv", "Tara"]
    last_names  = ["Sharma", "Verma", "Mukherjee", "Banerjee", "Patel", "Iyer", "Agarwal", "Chatterjee", "Gupta", "Das"]
    segments = ["Retail", "SMB", "Enterprise"]
    cities   = ["Kolkata", "Mumbai", "Delhi", "Bengaluru", "Pune", "Hyderabad", "Chennai", "Ahmedabad"]
    states   = ["WB", "MH", "DL", "KA", "MH", "TS", "TN", "GJ"]

    names = []
    emails = []
    for i in range(n_customers):
        fn = rng.choice(first_names)
        ln = rng.choice(last_names)
        name = f"{fn} {ln}"
        handle = f"{fn.lower()}.{ln.lower()}{100+i}"
        email = f"{handle}@example.com"
        names.append(name)
        emails.append(email)

    df = pd.DataFrame({
        "customer_id": [f"CUST{1000+i}" for i in range(n_customers)],
        "customer_name": names,
        "email": emails,
        "segment": rng.choice(segments, size=n_customers, p=[0.6, 0.3, 0.1]),
        "city": rng.choice(cities, size=n_customers),
        "state": rng.choice(states, size=n_customers)
    })
    return df

def create_orders(n_lines: int = 200, n_customers: int = 50, seed: int = 456) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    catalog = [
        ("Wireless Mouse",         "Electronics", 899.00),
        ("USB-C Cable",            "Electronics", 299.00),
        ("Laptop Stand",           "Accessories", 1499.00),
        ("Bluetooth Headphones",   "Electronics", 2999.00),
        ("Notebook (A5)",          "Stationery", 99.00),
        ("Gel Pen Pack (10)",      "Stationery", 149.00),
        ("Water Bottle (1L)",      "Home & Kitchen", 499.00),
        ("Coffee Mug",             "Home & Kitchen", 349.00),
        ("Desk Lamp",              "Home & Kitchen", 1299.00),
        ("Backpack",               "Accessories", 1999.00),
        ("Power Bank (10k mAh)",   "Electronics", 1799.00),
        ("Wireless Keyboard",      "Electronics", 1599.00),
        ("HDMI Cable",             "Electronics", 399.00),
        ("Portable SSD (500GB)",   "Electronics", 5499.00),
        ("Sticky Notes (100)",     "Stationery", 79.00),
        ("Phone Case",             "Accessories", 399.00),
        ("Desk Organizer",         "Home & Kitchen", 899.00),
        ("Whiteboard Marker (4)",  "Stationery", 129.00),
        ("Surge Protector",        "Electronics", 899.00),
        ("Fitness Band",           "Electronics", 3499.00),
    ]
    product_names = [c[0] for c in catalog]
    product_prices = {c[0]: c[2] for c in catalog}
    product_cats   = {c[0]: c[1] for c in catalog}

    # Simulate ~80–120 unique orders, distributed across n_lines
    n_orders = int(rng.integers(low=80, high=121))
    order_ids = [f"ORD{2025}{i:05d}" for i in range(1, n_orders + 1)]

    assigned_orders = rng.choice(order_ids, size=n_lines, replace=True)
    customer_ids = [f"CUST{1000+i}" for i in rng.integers(0, n_customers, size=n_lines)]

    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)
    days_span = (end_date - start_date).days + 1
    order_dates = [start_date + timedelta(days=int(d)) for d in rng.integers(0, days_span, size=n_lines)]

    # Popularity weights (make some items more frequent)
    popularity_weights = np.linspace(2, 1, num=len(product_names))
    popularity_weights = popularity_weights / popularity_weights.sum()
    chosen_products = rng.choice(product_names, size=n_lines, p=popularity_weights)

    quantities = rng.choice([1, 2, 3, 4, 5], size=n_lines, p=[0.5, 0.25, 0.15, 0.07, 0.03])
    statuses = rng.choice(["Completed", "Returned", "Cancelled"], size=n_lines, p=[0.75, 0.1, 0.15])

    df = pd.DataFrame({
        "order_id": assigned_orders,
        "customer_id": customer_ids,
        "order_date": order_dates,
        "product_name": chosen_products,
        "category": [product_cats[p] for p in chosen_products],
        "unit_price": [product_prices[p] for p in chosen_products],
        "quantity": quantities,
        "status": statuses
    })
    df["line_amount"] = df["unit_price"] * df["quantity"]
    df = df.sort_values(["order_date", "order_id"]).reset_index(drop=True)
    return df

def main():
    customers_df = create_customers(n_customers=50, seed=123)
    orders_df = create_orders(n_lines=200, n_customers=50, seed=456)

    customers_df.to_csv(CUSTOMERS_CSV, index=False)
    orders_df.to_csv(ORDERS_CSV, index=False)

    print(f"Created {Path(CUSTOMERS_CSV).resolve()}")
    print(f"Created {Path(ORDERS_CSV).resolve()}")
    print("\n=== customers.csv (sample) ===")
    print(customers_df.head().to_string(index=False))
    print("\n=== orders.csv (sample) ===")
    print(orders_df.head().to_string(index=False))

if __name__ == "__main__":
    main()
