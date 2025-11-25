#Given a list with duplicates, convert it to a set and then back to a list, preserving the original order of
#first occurrences.

l1=[1,2,2,6,4]
s1=set()
l2=[]

for i in l1:
    if i not in s1:
        s1.add(i)
        l2.append(i)

print(l2)