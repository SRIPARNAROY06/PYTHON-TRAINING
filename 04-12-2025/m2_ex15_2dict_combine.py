def combine_sum_values_plain(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

d1 = {"a": 10, "b": 20, "c": 5}
d2 = {"b": 7, "c": 15, "d": 3}
print(combine_sum_values_plain(d1, d2))