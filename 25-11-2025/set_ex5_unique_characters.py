#Given a list of words, find all unique characters across all words combined, using sets.

l1=["day","dog","cat"]
unique=set()

for x in l1:
    for y in x:
        unique.add(y)

print(unique)
