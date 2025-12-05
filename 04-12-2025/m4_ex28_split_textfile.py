file_path = "sample.txt"

with open(file_path, "r") as f:
    lines = f.readlines()

mid = len(lines) // 2

with open("first_half.txt", "w") as f1:
    f1.writelines(lines[:mid])

with open("second_half.txt", "w") as f2:
    f2.writelines(lines[mid:])

