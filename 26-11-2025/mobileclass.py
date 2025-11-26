class Mobile:
    def __init__(self, brand,model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def up_storage(self,extra_storage):
        self.storage=self.storage + extra_storage


    def display(self):
        print(self.brand, self.model, self.storage)

m1=Mobile("Apple","17 Pro",128)
m1.display()
m1.up_storage(256)
m1.display()


