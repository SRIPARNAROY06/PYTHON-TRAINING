
def symmetric_diff_manual(set1, set2):
    return (set1 - set2) | (set2 - set1)

# Example usage:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = symmetric_diff_manual(a, b)
print(result)  # Output: {1, 2, 5, 6}
