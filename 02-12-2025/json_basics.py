import pandas as pd

# #Dataframe --2D
# df=pd.DataFrame({
#     "Name":["Aisha","Rahul","John","Neha","Imran"],
#     "Marks":[85,92,78,65,55],
#     "City":["Mumbai","Delhi","Chennai","Bangalore","Hyderabad"],
#     "Age":[22,25,23,21,24]
# })
#
# #write a json file
# df.to_json("students.json", orient="records", indent=4)
# print("JSON file created")
#
# #read the same json file
# df=pd.read_json("students.json")
# print("JSON file read successfully")
# print(df)


df=pd.DataFrame({
     "Name":["Aisha","Rahul","John","Neha","Imran"],
     "Marks":[85,None,78,None,55],
     "City":["Mumbai","Delhi",None,"Bangalore",None],
    "Age":[22,25,None,21,24]
 })

print(df.isnull())
print(df.isnull().sum())
print(df.replace("", None).isnull().sum())

