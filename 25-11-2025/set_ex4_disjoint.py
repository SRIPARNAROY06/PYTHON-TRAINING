#Check whether two sets are disjoint without using the built-in method.
s1={1,2,3,4}
s2={4,5,6,7}
disjoint=True

for i in s1:
    for j in s2:
        if i==j:
            disjoint=False
            break
    if not disjoint:
        break
if disjoint:
    print("sets ate disjoint")
else:
    print("sets not disjoint")