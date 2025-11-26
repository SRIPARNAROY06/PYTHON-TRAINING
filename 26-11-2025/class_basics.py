# class Student:
#     pass
#
# s1=Student() #new -- new object is being created. In Python there i sno new
# s2=Student() #when an object is created , it takes up some space in RAM

#Example2
class Student:
    def __init__(self,name,age):#constructor #only two parameters:name and age
        self.name=name #self is the object of the current class
        self.age=age

s3=Student("Sriparna",22)
s4=Student("Samson",23)
print(s3.name, s3.age)
print(s4.name)


