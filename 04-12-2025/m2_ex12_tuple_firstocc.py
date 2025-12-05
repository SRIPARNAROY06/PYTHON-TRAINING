def unique_names(names: tuple):
    seen = set()
    out = []
    for name in names:
        if name not in seen:
            seen.add(name)
            out.append(name)
    return tuple(out)

# Example
names = ("Asha", "Ravi", "Asha", "Imran", "Ravi", "Leena")
print(unique_names(names))