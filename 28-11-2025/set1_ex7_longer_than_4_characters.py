
def filter_long_strings(strings):
    return [s for s in strings if len(s) > 4]

# Example usage:
words = ["apple", "cat", "banana", "dog", "elephant"]
result = filter_long_strings(words)
print(result)  # Output: ['apple', 'banana', 'elephant']
