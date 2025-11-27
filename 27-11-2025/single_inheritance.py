#Example 1
class Company:
    def __init__(self, comp_name):
        self.comp_name = comp_name


class Employee(Company):
    def __init__(self,comp_name, emp_name,emp_id):
        super().__init__(comp_name)
        self.emp_name = emp_name
        self.emp_id = emp_id

e1=Employee("EY", "Sriparna", 101)
e2=Employee("IBM", "Eshika", 203)
print(e1.comp_name, e1.emp_name,e1.emp_id)
print(e2.comp_name, e2.emp_name,e2.emp_id)




#Example2

class Vehicle:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand,model,year,fuel_type):
        super().__init__(brand,model)
        self.year = year
        self.fuel_type = fuel_type

c1=Car("Honda","City",2017,"Petrol")
print(c1.year)
print(c1.fuel_type)
print(c1.brand)
print(c1.model)


