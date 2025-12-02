import pandas as pd
df=pd.read_csv("retails_50.csv")
#print(df.head())

# print(df.info()) #Date should be date object not object
# print(df.describe()) #only work on numeric columns
# print(df.isnull().sum())#no nulls therefore good data


df["Date"]=pd.to_datetime(df["Date"])
#print(df.info())

df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day"]=df["Date"].dt.day

#print(df)

# high_elec=df[(df["Category"]=="Electronics") & (df["TotalPrice"]>1000)]
# print(high_elec)
#
# sorted_df=df.sort_values("TotalPrice", ascending=False)
# category_sales=df.groupby("Category")["TotalPrice"].sum()
# print(category_sales)
#
# store_avg=df.groupby("Store")["TotalPrice"].mean()
# print(store_avg)
#
# city_orders=df.groupby("City")["OrderID"].count()
# print(city_orders)

customers=pd.DataFrame({
    "CustomerType": ["New","Returning"],
    "Discount":[5,10]
})
merged=df.merge(customers, on="CustomerType", how="left")
print(merged)

