numbers=(33,20,30,60,50)
max=numbers[0]
min=numbers[0]
for x in numbers:
    if x>max:
        max=x
for x in numbers:
    if x<min:
        min=x

print(max,min)
