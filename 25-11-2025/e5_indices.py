num=[5, 2, 7, 5, 9, 5, 3]
n=int(input("Enter a number"))
l1=[]
for i in range(0,len(num)):
    if num[i]==n:
        l1.append(i)

print(l1)