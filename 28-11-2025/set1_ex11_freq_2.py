
def elements_with_freq_two(lst):
    seen = set()
    freq_two = set()
    for item in lst:
        if item in seen:
            freq_two.add(item)
        else:
            seen.add(item)
    return freq_two

# Example usage:
data = [1, 2, 3, 2, 4, 1, 5, 1]
result = elements_with_freq_two(data)
print(result)  # Output: {2}
