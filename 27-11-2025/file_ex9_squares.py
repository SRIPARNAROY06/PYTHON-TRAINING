with open("numbers.text","w") as f:
    for i in range(1,11):
        square=i**2
        f.write(str(square) +"\n")

with open("numbers.text","r") as f:
    print(f.read())
