
import csv

def print_high_marks(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['marks']) > 75:
                print(row)


print_high_marks("students.csv")
