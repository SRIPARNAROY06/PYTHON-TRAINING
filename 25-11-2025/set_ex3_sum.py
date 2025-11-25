#Given a set of numbers, find all pairs that sum up to a target number.
# Example:
#
# Set = {2, 4, 6, 8, 10}
# Target = 12
# Output: (2, 10), (4, 8), (6, 6)
# Without reusing same pairs twice.

s1={2, 4, 6, 8, 10}
target=12
pairs=[]

for x in s1:
    for y in s1:
        if x<=y and x+y==target:
            pairs.append((x,y))

print(pairs)
