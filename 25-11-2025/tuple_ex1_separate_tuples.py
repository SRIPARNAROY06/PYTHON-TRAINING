#Given a tuple containing both numbers and strings, separate them into two tuples: one containing only
#numbers and one containing only strings.

tp1=(12,"cat","dog",23,56,"donkey")
tp2=()
tp3=()
for x in tp1:
    if isinstance(x,int):
        tp2=tp2+(x,)
    else:
        tp3=tp3+(x,)

print(tp2)
print(tp3)



