
def combine_dicts(dict1, dict2):
    combined = {}
    for key in set(dict1) | set(dict2):  # Union of keys
        if key in dict1 and key in dict2:
            combined[key] = [dict1[key], dict2[key]]
        elif key in dict1:
            combined[key] = dict1[key]
        else:
            combined[key] = dict2[key]
    return combined

# Example usage:
dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'b': 4, 'c': 5, 'd': 6}

result = combine_dicts(dict_a, dict_b)
print(result)
# Output: {'a': 1, 'b': [2, 4], 'c': [3, 5], 'd': 6}
