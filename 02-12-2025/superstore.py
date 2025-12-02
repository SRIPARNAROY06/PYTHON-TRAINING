import pandas as pd
df=pd.read_csv("superstore_details.csv")
# #Exercise1-5
# print(df.head(10))
# print(df.shape)
# print(df.dtypes)
# print(df.isnull().sum())
# df["OrderDate"]=pd.to_datetime(df["OrderDate"])
# df["ShipDate"]=pd.to_datetime(df["ShipDate"])
# print(df)
# print(df.dtypes)

#Exercise 6-10
df["OrderDate"] = pd.to_datetime(df["OrderDate"], format="%Y-%m-%d", errors="coerce")
df["ShipDate"] = pd.to_datetime(df["ShipDate"], format="%Y-%m-%d", errors="coerce")
df["ShippingDays"] = (df["ShipDate"] - df["OrderDate"]).dt.days
df["ProfitMargin"]=df["Profit"]/df["Sales"]
df["CustomerName"] = df["CustomerName"].apply(lambda x: str(x).title())
df=df[df["Sales"]>0]
df["Discount"] = df["Discount"] * 100
df.to_csv("orders_discount_percentage.csv", index=False)

#Exercise 11-15
# region=df[df["Region"]=="West"]
# print(region)
# tech_category=df[(df["Category"] == "Technology") & (df["Sales"] > 400)]
# print(tech_category)
# pdt_returned=df[df["Returned"]=="Yes"]
# print(pdt_returned)
# furniture_orders=df[(df["Category"] == "Furniture") & (df["ShipDate"] > "2024-01-20")]
# print(furniture_orders)
# orders_profit=df[df["Profit"]<20]
# print(orders_profit)

#Exercise 16-20
# sorted_sales = df.sort_values("Sales", ascending=False)
# print(sorted_sales[["CustomerName", "Sales"]])
# sorted_profit_margin = df.sort_values("ProfitMargin", ascending=False)
# print(sorted_profit_margin[["CustomerName", "ProfitMargin"]])
# sorted_region_city=df.sort_values(["Region","City"])
# print(sorted_region_city[["CustomerName", "Region", "City"]])
# cust_name=df.sort_values("CustomerName", ascending=True)
# print(cust_name["CustomerName"])


#Exercise 21-26
total_sales=df.groupby("Region")["Sales"].sum()
#print(total_sales)
cat_avg=df.groupby("Category")["Profit"].mean()
#print(cat_avg)
count_orders=df.groupby("CustomerName")["OrderID"].count()
#print(count_orders)
total_quantity=df.groupby("Segment")["Quantity"].sum()
#print(total_quantity)
shipping_days=df.groupby("Category")["ShippingDays"].mean()
#print(shipping_days)


