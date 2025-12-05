def merge_to_dict(keys, values):
    return dict(zip(keys, values))

list1 = ["p01", "p02", "p03"]
list2 = [199, 299, 399]
print(merge_to_dict(list1, list2))   
