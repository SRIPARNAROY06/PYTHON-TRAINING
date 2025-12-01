import pandas as pd

s=pd.Series([10,20,30,40]) #1D data
print(s)

#Dataframe --2D
data={
    "Name":["Aisha","Rahul","John"],
    "Marks":[85,92,78]
}

df=pd.DataFrame(data)
print(df)