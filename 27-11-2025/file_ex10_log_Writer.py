from datetime import datetime
with open("date.txt","a") as f:
    f.write(f"{datetime.now()} --Application Started\n")

print("Contents of date.txt are: ")

with open("date.txt","r") as f:
    print(f.read())

