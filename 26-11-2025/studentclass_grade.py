class Student:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1+self.m2+self.m3

    def percentage(self):
        return (self.total()/300)*100

    def grade(self):
        a=self.percentage()
        if a>90:
            return "A"
        elif a>80:
            return "B"
        elif a>70:
            return "C"
        else:
            return "D"


    def display(self):
        print("Name:",self.name)
        print("Marks:",self.m1,self.m2,self.m3)
        print("Total:",self.total())
        print("Percentage:",self.percentage())
        print("Grade:",self.grade())

#creating an object
s1=Student("Alex",10,20,30)
s1.display()
