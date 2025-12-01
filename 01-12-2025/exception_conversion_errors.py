def convert_to_integers(lst):
    converted = []
    for item in lst:
        try:
            converted.append(int(item))
        except ValueError:
            print(f"Error: Cannot convert '{item}' to integer.")
    return converted


data = ["10", "20", "abc", "30", "4.5", "xyz"]
result = convert_to_integers(data)
print("Converted list:", result)
