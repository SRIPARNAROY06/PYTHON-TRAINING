import json

json_file = "products.json"
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Phone", "price": 20000},
    {"name": "Tablet", "price": 15000}
]

with open(json_file, "w") as f:
    json.dump(products, f)


with open(json_file, "r") as f:
    products = json.load(f)

for p in products:
    p["price"] = round(p["price"] * 0.9, 2)

with open(json_file, "w") as f:
    json.dump(products, f)

