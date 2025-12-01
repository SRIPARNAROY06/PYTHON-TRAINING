import pandas as pd

s=pd.Series([10,20,30,40]) #1D data
print(s)

#Dataframe --2D
data={
    "Name":["Aisha","Rahul","John","Neha","Imran"],
    "Marks":[85,92,78,65,55],
    "City":["Mumbai","Delhi","Chennai","Bangalore","Hyderabad"],
    "Age":[22,25,23,21,24]
}

df=pd.DataFrame(data)
df.to_csv("students.csv",index=False)
# print("CSV file created")
#print(df)
#
# print(df.head(2))
# print(df.tail(2))
# print(df.shape)
# print(df.columns)
# print(df.describe())


# print(df["Name"])
# print(df[["Name","Marks"]])
#
# #FILTERS
# high_scores=df[df["Marks"]>70]
# print(high_scores)
#
# filtered=df[(df["Marks"]>70) & (df["Age"]>22)]
# print(filtered)

# df["Result"]=df["Marks"].apply(lambda x: "Pass" if x>=60 else "Fail")
# print(df)
#
# sorted_df=df.sort_values("Marks",ascending=False)
# print(sorted_df)

#create missing value
# df2=df.copy()
# df2.loc[2,"City"]=None
# print(df2)
# print(df2.isnull().sum())
# 
# 
# #NA --None --0--""
# df2_filled=df2.fillna("Unknown")
# print(df2_filled)


city_count=df.groupby("City")["Name"].count()
print(city_count)

avg_marks=df.groupby("City")["Marks"].mean()
print(avg_marks)

