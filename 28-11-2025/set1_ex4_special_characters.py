s=input("Enter a string: ")
result=""
for ch in s:
    if ch.isalpha():
        result=result+ch
print(result)
