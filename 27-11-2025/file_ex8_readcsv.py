import csv

with open("students.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name","marks"])
    writer.writerow(["Sriparna","85"])
    writer.writerow(["Ahana","90"])



#Reading from the same file
with open("students.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name=row[0]
        marks=row[1]
        print(f"Name:{name} Marks:{marks}")