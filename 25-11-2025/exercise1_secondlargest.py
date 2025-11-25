nums=[23,89,12,78,55,42]
max=nums[0]
max2=nums[0]
for i in range(1,len(nums)):
    if nums[i]>max:
        max=nums[i]

for j in range(1,len(nums)):
    if nums[j]!=max:
        if(nums[j]>max2):
            max2=nums[j]

print(max2)
