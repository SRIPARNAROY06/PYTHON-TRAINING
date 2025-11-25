nums = [10, 3, 5, 12, 8, 7, 1]
even=[]
odd=[]
for i in nums:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)