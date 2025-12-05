
# clean_outliers_iqr.py
import pandas as pd

df = pd.read_csv('orders.csv')

num_cols = df.select_dtypes(include='number').columns

Q1 = df[num_cols].quantile(0.25)
Q3 = df[num_cols].quantile(0.75)
IQR = Q3 - Q1


lower_bounds = Q1 - 1.5 * IQR
upper_bounds = Q3 + 1.5 * IQR


mask = ((df[num_cols] >= lower_bounds) & (df[num_cols] <= upper_bounds)).all(axis=1)
clean_df = df[mask].copy()


print("Original rows:", len(df))
print("Cleaned rows :", len(clean_df))
print("\nCleaned dataset (first 10 rows):")
print(clean_df.head(10).to_string(index=False))

# Optional: save cleaned data
clean_df.to_csv('cleaned_output.csv', index=False)
