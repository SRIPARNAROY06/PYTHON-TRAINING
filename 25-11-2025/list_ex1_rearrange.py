#Given a list of integers, rearrange the list so that all negative numbers appear first and all positive
#numbers appear later, without using additional predefined functions like sort() .

l1=[7,-1,8]
l2=[]
l3=[]
for i in l1:
    if i<0:
        l2.append(i)
    else:
        l3.append(i)

print(l2 + l3)

