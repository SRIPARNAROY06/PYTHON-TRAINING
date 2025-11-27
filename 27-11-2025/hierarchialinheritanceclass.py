# #example1
class Shape:
    def __init__(self, color):
        self.color = color


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area_circle(self):
        return 3.14*self.radius**2

class Rectangle(Shape):
    def __init__(self, color, length, breadth):
        super().__init__(color)
        self.length = length
        self.breadth = breadth

    def area_rectangle(self):
        return self.length*self.breadth


class Triangle(Shape):
    def __init__(self, color,base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def area_triangle(self):
        return 0.5*self.base*self.height


shape1=Circle("Red",10)
print(shape1.area_circle())


#Example2
class Employee:
    def __init__(self, emp_id,emp_name,emp_age):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age

    def print_emp(self):
        print("Employee ID with Name and Age:", self.emp_id,self.emp_name,self.emp_age)

class Manager(Employee):
    def __init__(self,emp_id,emp_name,emp_age,salary,team_size):
        super().__init__(emp_id,emp_name,emp_age)
        self.salary = salary
        self.team_size = team_size
    def print_manager(self):
        print("Manager Salary:", self.salary)
        print("Team Size:", self.team_size)

class Developer(Employee):
    def __init__(self,emp_id,emp_name,emp_age,salary,programming_language,role):
        super().__init__(emp_id, emp_name, emp_age)
        self.salary = salary
        self.programming_language = programming_language
        self.role = role

    def print_developer(self):
        print("Developer Salary:", self.salary)
        print("Programming Language:", self.programming_language)
        print("Role:", self.role)

class Tester(Developer):
    def __init__(self,emp_id,emp_name,emp_age,salary):
        super().__init__(emp_id, emp_name, emp_age)
        self.salary = salary

    def print_tester(self):
        print("Tester Salary:", self.salary)


employee=Developer(101,"Anne",34,450000,"Java","Senior Developer")
employee.print_emp()
employee.print_developer()





