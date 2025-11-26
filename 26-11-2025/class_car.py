class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):
        print("Brand:", self.brand)
        print("Model:",self.model)
        print("Price:",self.price)

#Creating three Car Objects
car1=Car("Toyota", "Fortuner", 4500000)
car2=Car("Hyundai", "Creta", 1800000)
car3=Car("Tesla", "Model 3", 2000000)

#displaying details
car1.display()
print()
car2.display()
print()
car3.display()
print()



