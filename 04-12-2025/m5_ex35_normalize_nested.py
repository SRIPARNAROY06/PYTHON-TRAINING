import json
import pandas as pd
from pathlib import Path

import pandas as pd

df = pd.read_csv("customers.csv")
df.to_json("customers.json", orient="records", indent=2)
print("Converted customers.csv to customers.json")


INPUT_JSON = "customers.json"
OUT_FLAT_CSV = "customers_flat.csv"
OUT_ORDERS_CSV = "customers_orders.csv"


def load_json(path: str | Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_flat(data):
    return pd.json_normalize(data, max_level=1)


def normalize_list_field(data, list_field: str):
    records = []
    for entry in data:
        list_items = entry.get(list_field, [])
        if isinstance(list_items, list) and len(list_items) > 0:
            for item in list_items:
                base = {k: v for k, v in entry.items() if k != list_field}
                records.append({**base, **{f"{list_field}": item}})
        else:
            base = {k: v for k, v in entry.items() if k != list_field}
            records.append({**base, **{f"{list_field}": None}})
    df = pd.json_normalize(records, sep=".")
    if f"{list_field}" in df.columns:
        nested_cols = [c for c in df.columns if c.startswith(f"{list_field}.")]
        if nested_cols:
            pass
    return df


def main():
    in_path = Path(INPUT_JSON)
    if not in_path.exists():
        raise FileNotFoundError(f"Input JSON not found: {in_path.resolve()}")

    data = load_json(in_path)

    df_flat = normalize_flat(data)
    df_flat.to_csv(OUT_FLAT_CSV, index=False)
    print(f"Saved flat normalization -> {Path(OUT_FLAT_CSV).resolve()}")
    print("\n=== customers_flat (sample) ===")
    print(df_flat.head().to_string(index=False))

    list_fields = []
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        for k, v in data[0].items():
            if isinstance(v, list):
                list_fields.append(k)

    if list_fields:
        for lf in list_fields:
            df_list = normalize_list_field(data, lf)
            out_path = Path(OUT_ORDERS_CSV if lf == "orders" else f"customers_{lf}.csv")
            df_list.to_csv(out_path, index=False)
            print(f"\nSaved exploded list '{lf}' -> {out_path.resolve()}")
            print(f"=== customers_{lf} (sample) ===")
            print(df_list.head().to_string(index=False))
    else:
        print("\nℹ️ No top-level list fields detected to explode.")


if __name__ == "__main__":
    main()

