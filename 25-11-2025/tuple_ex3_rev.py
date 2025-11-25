# Create a tuple of words and return a new tuple where each word is reversed.
# Input: ("python", "cloud", "data")
# Output: ("nohtyp", "duolc", "atad")

t1=("python", "cloud", "data")
t2=()
for x in t1:
    rev=""
    for j in x:
        rev=j+rev
    t2=t2+(rev,)

print(t2)


