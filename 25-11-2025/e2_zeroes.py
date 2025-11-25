#move all zeroes to the side
nums=[0,3,0,5,7,0,9]
temp=[]
zeroes=[]
for i in range(0,len(nums)):
    if nums[i]!=0:
        temp.append(nums[i])
    else:
        zeroes.append(nums[i])

print(temp + zeroes)

