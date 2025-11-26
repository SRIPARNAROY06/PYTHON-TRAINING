class Customer:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

    def eligible(self):
        return (self.age>25)

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("City:",self.city)
        print("Eligible:",self.eligible())

c1= Customer("Ankur",22,"Mumbai")
c1.display()