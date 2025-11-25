student={
    "name":"Sriparna",
    "age":22,
    "city": "Kolkata"
}

# print(student["name"])#to get data use this approach or use .get
# print(student["age"])
# print(student.get("email"))
#
# student["email"]="sriparna.roy12@gmail.com"
# student["city"]="Dubai"
#
# #3 ways to delete in dictionary
# student.pop("age")#remove by key
# del student["city"] #delete
# student.clear() #empty dictionary


# print(student.keys())
# print(student.values())

for k in student.keys():
    print(k)
for v in student.values():
    print(v)
for k,v in student.items():
    print(k,v)