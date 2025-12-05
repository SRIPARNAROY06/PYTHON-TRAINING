import csv
import json

csv_file = "employees.csv"
json_file = "employees.json"

with open(csv_file, "r") as f:
       reader = csv.DictReader(f)
       data = list(reader)

with open(json_file, "w") as f:
    json.dump(data, f)

