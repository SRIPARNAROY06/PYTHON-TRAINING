#Given a list of strings, remove all strings whose length is less than 3.
list1=["cat","dog","ankur","donkey"]
new_list=[]

for x in list1:
    if len(x)>3:
        new_list.append(x)

print(new_list)
