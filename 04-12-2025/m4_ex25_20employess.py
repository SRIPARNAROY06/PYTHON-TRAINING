import csv
csv_file = "employees.csv"

with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ID", "Name", "Salary"])
    writer.writeheader()
    for i in range(1, 21):
        writer.writerow({"ID": i, "Name": f"Employee{i}", "Salary": 50000 + i * 1000})

print("CSV file created.")
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    employees = list(reader)

print("Employees loaded:")
for emp in employees[:5]:
    print(emp)
