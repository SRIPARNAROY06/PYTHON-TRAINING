# #Given a dictionary of student marks:
# {"A": 85, "B": 92, "C": 78, "D": 92}
# Print all keys that have the maximum value without using max() .

student_marks={"A": 85, "B": 92, "C": 78, "D": 92}
max_value=None
for x in student_marks:
    if max_value is None or x>max_value:
        max_value=x

print(max_value)