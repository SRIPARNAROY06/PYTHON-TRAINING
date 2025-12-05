import pandas as pd
df = pd.read_csv("orders.csv")
if "line_amount" not in df.columns:
    df["line_amount"] = df["unit_price"] * df["quantity"]

customer_totals = df.groupby("customer_id")["line_amount"].sum()
high_spenders = customer_totals[customer_totals > 5000].index
filtered_df = df[df["customer_id"].isin(high_spenders)]
print(filtered_df.head())
filtered_df.to_csv("high_spend_transactions.csv", index=False)
