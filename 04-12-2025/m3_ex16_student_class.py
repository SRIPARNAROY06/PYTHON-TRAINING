class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def grade(self):
        """Return grade based on marks."""
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}, Grade: {self.grade()}")


if __name__ == "__main__":
    s1 = Student(101, "Asha", 86)
    s2 = Student(102, "Ravi", 92)

    s1.display()
