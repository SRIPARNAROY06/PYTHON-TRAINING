with open("notes.txt","a") as f:
    f.write("This is an appended line\n")

#Reading from the same file
with open("notes.txt","r") as f:
    content=f.read()
    print(content)