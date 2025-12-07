items={
    "apple":50,
    "banana":120,
    "orange":30,
    "chips":56,
    "mango":140,
}

to_delete=[]
for item,price in items.items():
    if price<100:
        to_delete.append(item)

for item in to_delete:
    del items[item]

print(items)