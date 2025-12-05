
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

INPUT_CSV = "retail_100.csv"
OUTPUT_CSV = "category_report.csv"

def create_retail_dataset(n_rows: int = 100, seed: int = 42) -> pd.DataFrame:
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

    n_orders = int(rng.integers(low=40, high=61))
    order_ids = [f"ORD{2025}{i:04d}" for i in range(1, n_orders + 1)]
    assigned_orders = rng.choice(order_ids, size=n_rows, replace=True)

    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)
    days_span = (end_date - start_date).days + 1
    order_dates = [start_date + timedelta(days=int(d)) for d in rng.integers(0, days_span, size=n_rows)]

    customer_ids = [f"CUST{1000 + int(x)}" for x in rng.integers(0, 300, size=n_rows)]
    popularity_weights = np.linspace(2, 1, num=len(product_names))
    popularity_weights = popularity_weights / popularity_weights.sum()
    chosen_products = rng.choice(product_names, size=n_rows, p=popularity_weights)
    quantities = rng.choice([1, 2, 3, 4, 5], size=n_rows, p=[0.45, 0.25, 0.15, 0.1, 0.05])

    statuses = rng.choice(
        ["Completed", "Completed", "Completed", "Returned", "Cancelled"],
        size=n_rows,
        p=[0.6, 0.15, 0.05, 0.1, 0.1]
    )

    df = pd.DataFrame({
        "order_id": assigned_orders,
        "order_date": order_dates,
        "customer_id": customer_ids,
        "product_name": chosen_products,
        "category": [product_cats[p] for p in chosen_products],
        "unit_price": [product_prices[p] for p in chosen_products],
        "quantity": quantities,
        "status": statuses
    })
    df["line_amount"] = df["unit_price"] * df["quantity"]
    df = df.sort_values(["order_date", "order_id"]).reset_index(drop=True)
    return df

def ensure_line_amount(df: pd.DataFrame) -> pd.DataFrame:
    if "line_amount" not in df.columns:
        price_col = "price" if "price" in df.columns else "unit_price"
        if price_col not in df.columns or "quantity" not in df.columns:
            raise ValueError("Dataset must have price/unit_price and quantity to compute line_amount.")
        df["line_amount"] = df[price_col] * df["quantity"]
    return df

def category_aggregates(df: pd.DataFrame) -> pd.DataFrame:
    df = ensure_line_amount(df.copy())
    price_col = "price" if "price" in df.columns else "unit_price"
    result = (
        df.groupby("category")
          .agg(total_sales=("line_amount", "sum"),
               orders_count=("order_id", "nunique"),
               average_price=(price_col, "mean"))
          .reset_index()
    )
    return result

def main():
    in_path = Path(INPUT_CSV)
    if not in_path.exists():
        print(f"Input file not found at {in_path.resolve()}. Creating a synthetic dataset...")
        df = create_retail_dataset(n_rows=100, seed=42)
        df.to_csv(in_path, index=False)
        print(f"Created {in_path.resolve()}")

    df = pd.read_csv(in_path, parse_dates=["order_date"])
    report = category_aggregates(df)

    print("\n=== Category-wise Report ===")
    print(report.to_string(index=False))

    out_path = Path(OUTPUT_CSV)
    report.to_csv(out_path, index=False)
    print(f"\nReport saved")
    print(f"\nReport saved to: {out_path.resolve()}")

if __name__ == "__main__":
    main()
