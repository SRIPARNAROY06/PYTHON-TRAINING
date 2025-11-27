#Writing to a file
with open("sample.txt","w") as f:
    f.write("Hello,this is the first line. \n")
    f.write("This file was created using Python. \n")

#Reading from the same file
with open("sample.txt","r") as f:
    content=f.read()
    print(content)