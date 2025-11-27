with open("source.txt","w") as f:
    f.write("winter is here")

#Reading from the same file
with open("source.txt","r") as first_file,open("backup.txt","w") as second_file:
    for line in first_file:
        second_file.write(line)
