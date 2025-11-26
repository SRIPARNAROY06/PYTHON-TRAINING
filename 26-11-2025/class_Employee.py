class Employee:
    def __init__(self,emp_id, name, department, salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary

    def display(self):
        print("Employee ID:",self.emp_id)
        print("Name:",self.name)
        print("Department:",self.department)
        print("Salary:",self.salary)

#Creating employee objects
e1=Employee(101, "Sriparna", "DET", 350000)
e2=Employee(102,"Ayushi","IT", 450000)
e1.display()
print()
e2.display()
print()
