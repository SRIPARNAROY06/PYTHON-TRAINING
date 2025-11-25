#Given a list, create a new list that contains only those elements which appear more than once. Do not
#use set() .
l1=[1,22,33,32,7,5,22,33]
new_list=[]
for x in l1:
    if l1.count(x)>1 and x not in new_list:
        new_list.append(x)
print(new_list)