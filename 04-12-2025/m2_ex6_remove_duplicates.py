def unique_in_order(prices):
    return list(dict.fromkeys(prices))

# Example
prices = [199, 299, 199, 499, 299, 299, 599]
print(unique_in_order(prices))
