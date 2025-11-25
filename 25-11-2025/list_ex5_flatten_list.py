#Flatten a nested list using loops only.
# Example:
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]

nested=[[1, 2], [3, 4], [5]]
flattened=[]
for i in nested:
    for j in i:
        flattened.append(j)

print(flattened)