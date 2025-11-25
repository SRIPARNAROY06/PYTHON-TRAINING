#Given a tuple of numbers, determine whether it is strictly increasing.

t1=(1,2,33,44)
increasing=True

for i in range(len(t1)-1):
    if t1[i]>t1[i+1]:
        increasing=False
        break
if increasing:
    print("Strictly Increasing")
else:
    print("Not Strictly Increasing")