employees={
    "e1":{"dept":"IT"},
    "e2":{"dept":"HR"},
    "e3":{"dept":"IT"},
}
dept_count={}

for emp,data in employees.items():
    dept=data["dept"]
    if dept not in dept_count:
        dept_count[dept]=0
    dept_count[dept]+=1

print(dept_count)
