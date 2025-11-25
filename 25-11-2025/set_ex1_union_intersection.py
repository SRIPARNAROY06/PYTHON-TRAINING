#Given two sets, print the elements that are present in the union but not in the intersection.

s1={1,2,3,4}
s2={3,4,5,6}

union_s1=s1.union(s2)
intersection_s1=s1.intersection(s2)

print(union_s1 - intersection_s1)