
import pandas as pd
from pathlib import Path

INPUT_CSV = "retail_100.csv"
OUTPUT_CSV = "retail_100_cleaned.csv"

def fill_missing_values(df: pd.DataFrame):
    df = df.copy()
    num_cols = df.select_dtypes(include=["number"]).columns
    cat_cols = df.select_dtypes(exclude=["number"]).columns

    for c in num_cols:
        df[c] = df[c].fillna(df[c].median())

    for c in cat_cols:
        mode_vals = df[c].mode(dropna=True)
        if len(mode_vals) > 0:
            df[c] = df[c].fillna(mode_vals.iloc[0])
        else:
            # if no mode (e.g., all NaN), fill with empty string as a safe placeholder
            df[c] = df[c].fillna("")

    return df

def main():
    in_path = Path(INPUT_CSV)
    if not in_path.exists():
        raise FileNotFoundError(f"Input file not found: {in_path.resolve()}")

    df = pd.read_csv(in_path)

    print("=== Missing values (before) ===")
    print(df.isna().sum())

    cleaned = fill_missing_values(df)

    print("\n=== Missing values (after) ===")
    print(cleaned.isna().sum())

    cleaned.to_csv(OUTPUT_CSV, index=False)
    print(f"\nCleaned file saved to: {Path(OUTPUT_CSV).resolve()}")

if __name__ == "__main__":
    main()
