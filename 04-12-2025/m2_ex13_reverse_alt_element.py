def reverse_every_alternate_content(lst: list):
    out = lst[:]
    for i in range(1, len(out), 2):
        try:
            out[i] = out[i][::-1]
        except TypeError:
            pass
    return out

# Example
items = ["apple", "banana", "cherry", "date", "egg", "fig"]
print(reverse_every_alternate_content(items))
