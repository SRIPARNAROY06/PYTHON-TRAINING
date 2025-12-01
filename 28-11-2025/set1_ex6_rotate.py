#Rotate a list to the left by N positions using only loops.
l1=[1,3,45,23,11]
N=int(input("Enter the number"))

for i in range(N):
    first=l1[0]
    for j in range(len(l1)-1):
        l1[j]=l1[j+1]
    l1[-1]=first
print(l1)