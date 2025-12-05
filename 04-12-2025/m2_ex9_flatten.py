def flatten(nested):
    return [x for sub in nested for x in sub]

nested = [[1, 2], [3, 4], [5, 6]]
print(flatten(nested))
