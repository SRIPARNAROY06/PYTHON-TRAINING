import pandas as pd
from pathlib import Path

INPUT_CSV = "retail_100.csv"
OUTPUT_CSV = "retail_discounted.csv"


def add_discounted_price(df, percent=10):
    df = df.copy()
    if "unit_price" in df.columns:
        price_col = "unit_price"
    elif "price" in df.columns:
        price_col = "price"
    else:
        raise ValueError("No price column found in dataset.")

    df["DiscountedPrice"] = df[price_col] * (1 - percent / 100.0)
    return df


def main():
    in_path = Path(INPUT_CSV)
    if not in_path.exists():
        raise FileNotFoundError(f"Input file not found: {in_path.resolve()}")

    df = pd.read_csv(in_path, parse_dates=["order_date"])

    df = add_discounted_price(df, percent=10)

    # Show sample rows
    print("\n=== Sample with DiscountedPrice ===")
    print(df.head())

    # Save updated dataset
    out_path = Path(OUTPUT_CSV)
    df.to_csv(out_path, index=False)
    print(f"\n Updated file saved to: {out_path.resolve()}")


if __name__ == "__main__":
    main()