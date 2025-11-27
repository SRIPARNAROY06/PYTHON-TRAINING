with open("notes.txt","w") as f:
    f.write("My name is Sriparna Roy \n")
    f.write("I know Python, Java \n")
    f.write("Python is a versatile language\n")
    f.write("Working at EY \n")
    f.write("Stays in Kolkata \n")

#Reading from the same file
with open("notes.txt","r") as f:
    for line in f:
        if "Python" in line:
            print(line.strip())