#Inheritance
#Example1
# class Animal:
#     def speak(self):
#         print("Animal makes a sound")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
#
# d=Dog()
# d.speak()  #inherited
# d.bark()  #child's own method



#Example2
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name) #call parent constructor
        self.employee_id = employee_id

e=Employee("Sriparna", 101)
print(e.name)
print(e.employee_id)
