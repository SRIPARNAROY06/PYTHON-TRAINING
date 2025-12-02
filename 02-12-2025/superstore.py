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

#Example 27-31

# df['Month'] = df['OrderDate'].dt.to_period('M')
# pivot_sales = pd.pivot_table(df, index='Region', columns='Category', values='Sales', aggfunc='sum', fill_value=0)
# print("Pivot 1: Sales by Region and Category\n", pivot_sales, "\n")
#
#
# pivot_profit = pd.pivot_table(df, index='SubCategory', columns='Segment', values='Profit', aggfunc='sum', fill_value=0)
# print("Pivot 2: Profit by SubCategory and Segment\n", pivot_profit, "\n")
#
#
# pivot_returned = pd.pivot_table(df, index='Returned', columns='Region', values='OrderID', aggfunc='count', fill_value=0)
# print("Pivot 3: Count of Orders by Returned Status and Region\n", pivot_returned, "\n")
#
#
# pivot_avg_price = pd.pivot_table(df, index='Category', values='UnitPrice', aggfunc='mean')
# print("Pivot 4: Average UnitPrice per Category\n", pivot_avg_price, "\n")
#
# pivot_quantity = pd.pivot_table(df, index='Month', columns='Region', values='Quantity', aggfunc='sum', fill_value=0)
# print("Pivot 5: Quantity per Month\n", pivot_quantity, "\n")

#Example 32-35

segment_discount = pd.DataFrame({
    'Segment': ['Consumer', 'Corporate', 'Home Office'],
    'SegmentDiscount': [0.05, 0.08, 0.10]  # 5%, 8%, 10%
})
df = df.merge(segment_discount, on='Segment', how='left')
#print(df)
region_tax_table= pd.DataFrame({

    'Region': ['West', 'East', 'Central', 'South'],
    'RegionTax': [0.07, 0.06, 0.05, 0.08]  # 7%, 6%, 5%, 8%

})
df=df.merge(region_tax_table, on='Region', how='left')
#print(df[["RegionTax","Region"]])
cust_level_totals=df.groupby('CustomerID').agg(
    CustomerTotalSales=('Sales', 'sum'),
    CustomerTotalProfit=('Profit', 'sum')
).reset_index()
# df = df.merge(cust_level_totals, on='CustomerID', how='left')
# print(df)

pdt_level_profit=df.groupby('ProductName').agg(
    ProductTotalSales=('Sales', 'sum'),
    ProductTotalProfit=('Profit', 'sum')
).reset_index()
# df = df.merge(pdt_level_profit, on='ProductName', how='left')
# print(df)

#Example 36-40
df["OrderYear"]=df["OrderDate"].dt.year
df["OrderMonth"]=df["OrderDate"].dt.month
df["OrderDay"]=df["OrderDate"].dt.day
#print(df[['OrderDate', 'OrderYear', 'OrderMonth', 'OrderDay']].head())

df['OrderDayOfWeek'] = df['OrderDate'].dt.day_name()
#print(df["OrderDayOfWeek"].head())


df['ShipDelayDays'] = (df['ShipDate'] - df['OrderDate']).dt.days
orders_delayed = df[df['ShipDelayDays'] > 5]
#print(orders_delayed)



df['OrderMonth'] = df['OrderDate'].dt.strftime('%Y-%m')
monthly_sales = df.groupby('OrderMonth', as_index=False)['Sales'].sum()

fig = px.line(monthly_sales, x='OrderMonth', y='Sales',
             title='Monthly Sales Trend', markers=True)
fig.show()

print("Orders shipped in more than 5 days:\n", orders_delayed[['OrderID','OrderDate','ShipDate','ShipDelayDays']], "\n")
print("Monthly Sales Summary:\n", monthly_sales)

