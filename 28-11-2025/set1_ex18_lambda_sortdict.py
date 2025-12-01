
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

# Sort by age
sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)

