import pandas as pd

#Exercise 1
df=pd.read_csv("sales_data.csv")
# print(df.head(5))
# print(df.tail(5))
# print(df.columns)
# print(df.shape)


#Exercise 2
# df["Date"]=pd.to_datetime(df["Date"])
# df['Year'] = df['Date'].dt.year
# df['Month'] = df['Date'].dt.month
# df['Day'] = df['Date'].dt.day
# #df['Weekday'] = df['Date'].dt.day_name()
# df.to_csv("sales_data_with_date_parts.csv", index=False)
# print("Updated CSV file created successfully!")
# print(df.head())


#Exercise 3
# #Calculate total sales grouped by Store
# sales_by_store = df.groupby('Store')['TotalPrice'].sum().reset_index()
# print("Total Sales by Store:\n", sales_by_store)
#
# # Calculate total sales grouped by City
# sales_by_city = df.groupby('City')['TotalPrice'].sum().reset_index()
# print("\nTotal Sales by City:\n", sales_by_city)
#
# # Calculate total sales grouped by Category
# sales_by_category = df.groupby('Category')['TotalPrice'].sum().reset_index()
# print("\nTotal Sales by Category:\n", sales_by_category)

#Exercise 4
# top_5_orders = df.sort_values('TotalPrice', ascending=False).head(5)
# print("Top 5 Highest-Value Orders:")
# print(top_5_orders)



#Exercise 5

# filtered_df = df[(df['Category'] == 'Electronics') & (df['Quantity'] > 1)]
# print("Electronics products with Quantity > 1:")
# print(filtered_df)
#
# filtered_df.to_csv("electronics_quantity_gt1.csv", index=False)
# print("Filtered data saved to electronics_quantity_gt1.csv")

#Exercise 6
# df['Discount'] = df['CustomerType'].apply(lambda x: 0.10 if x == 'Returning' else 0.05)
# df['FinalPrice'] = df['TotalPrice'] * (1 - df['Discount'])
# print(df.head())
# df.to_csv("sales_data_with_discount.csv", index=False)
# print("Updated data saved to sales_data_with_discount.csv")

#Exercise 7

# payment_counts = df['PaymentMethod'].value_counts()
# print("Orders by Payment Method:")
# print(payment_counts)
#
# methods = ['Cash', 'Credit Card', 'UPI']
# filtered_counts = payment_counts[methods]
# print("\nFiltered counts:")
# print(filtered_counts)


#Exercise 8

# category_summary = df.groupby('Category').agg(
#     Total_Quantity=('Quantity', 'sum'),
#     Total_Revenue=('TotalPrice', 'sum')
# ).reset_index()
#
# print("Summary by Category:")
# print(category_summary)


#Exercise 9
# store_sales = df.groupby('Store')['TotalPrice'].sum().reset_index()
# top_store = store_sales.sort_values(by='TotalPrice', ascending=False).head(1)
# print("Store with the highest total sales:")
# print(top_store)

#Exercise 10

# filtered_df = df[df['Product'].str.contains('a', case=False, na=False)]
#
# print("Products containing 'a' or 'A':")
# print(filtered_df)
# filtered_df.to_csv("products_with_a.csv", index=False)
# print("Filtered data saved to products_with_a.csv")

#Exercise 11

# df['Date'] = pd.to_datetime(df['Date'])
#
# sorted_df = df.sort_values(by=['Date', 'TotalPrice'], ascending=[True, True])
# print("Dataset sorted by Date and then by TotalPrice:")
# print(sorted_df)
# sorted_df.to_csv("sorted_by_date_totalprice.csv", index=False)
# print("Sorted data saved to sorted_by_date_totalprice.csv")

#Exercise 12

# avg_revenue = df.groupby('CustomerType')['TotalPrice'].mean().reset_index()
# avg_revenue.columns = ['CustomerType', 'Avg_Revenue_Per_Order']
# print("Average Revenue per Order by CustomerType:")
# print(avg_revenue)


#Exercise 13

# pivot_table = pd.pivot_table(
#     df,
#     values='TotalPrice',
#     index='Category',
#     columns='PaymentMethod',
#     aggfunc='sum',
#     fill_value=0
# )
#
# print("Pivot Table (Category vs PaymentMethod):")
# print(pivot_table)
# pivot_table.to_csv("pivot_category_payment.csv")
# print("Pivot table saved to pivot_category_payment.csv")


#Exercise 14

# electronics_df = df[df['Category'] == 'Electronics']
# electronics_df.to_csv("electronics_only.csv", index=False)
# print("Electronics-only dataset saved to electronics_only.csv")

#Exercise 15


final_df = (
    df[df['Quantity'] >= 2]
      .query("Category == 'Apparel'")
      .assign(TotalValue=lambda x: x['Quantity'] * x['UnitPrice'])
      .sort_values(by='TotalValue', ascending=False)
      .reset_index(drop=True)  # Reset index
)


print("Final DataFrame:")
print(final_df)

final_df.to_csv("apparel_filtered_sorted.csv", index=False)
print("Final DataFrame saved to apparel_filtered_sorted.csv")





