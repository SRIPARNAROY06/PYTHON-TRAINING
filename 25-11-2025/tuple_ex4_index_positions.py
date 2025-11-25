#Write a program to find the index positions of a given value inside a tuple, without using index() .

t1=("cat",1,34,"dog")
value=34
indexes=[]
for x in range(len(t1)):
    if t1[x]== value:
        indexes.append(x)

print(indexes)
