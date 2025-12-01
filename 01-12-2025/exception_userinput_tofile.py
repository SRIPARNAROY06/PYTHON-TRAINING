filename="output.txt"

try:
    text=input("Please enter your text: ")
    file=open(filename,"w")
    file.write(text)

except IOError:
    print("I/O error")
    
else:
    print("I/O success")

finally:
    print("Closing file")


