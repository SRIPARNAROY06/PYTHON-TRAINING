def safe_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range."


numbers = [10, 20, 30]
print(safe_access(numbers, 1))   # Output: 20
print(safe_access(numbers, 5))   # Output: Error: Index 5 is out of range.
