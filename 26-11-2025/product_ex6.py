class Product():
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_cost(self):
        return (self.price * self.quantity)

    def display(self):
        print("Name:",self.name)
        print("Price:",self.price)
        print("Quantity:",self.quantity)
        print("Total cost:",self.total_cost())

a1=Product("Milkshake",100,200)
a1.display()