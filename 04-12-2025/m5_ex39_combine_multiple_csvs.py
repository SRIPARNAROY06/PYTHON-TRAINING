
import pandas as pd

files = ["customers.csv", "employees.csv", "category_report.csv"]


dfs = [pd.read_csv(f) for f in files]
merged = pd.concat(dfs, ignore_index=True)


final_df = merged.drop_duplicates()


print("Rows before dedup:", len(merged))
print("Rows after dedup :", len(final_df))
print(final_df.head())
