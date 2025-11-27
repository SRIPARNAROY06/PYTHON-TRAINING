with open("notes.txt","w") as f:
    f.write("My name is Sriparna Roy \n")
    f.write("Completed BTech in 2025 \n")
    f.write("Majored in ECE \n")
    f.write("Working at EY \n")
    f.write("Stays in Kolkata \n")

#Reading from the same file
with open("notes.txt","r") as f:
    content=f.read()
    print(content)