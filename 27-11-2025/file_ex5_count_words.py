with open("words_file.txt","w") as f:
    f.write("Apple and Mango\n")

#Reading from the same file
with open("words_file.txt","r") as f:
    content=f.read()
    text=len(content.split())
    print(content)
    print("Number of words:",text)
