#Example 1
class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name, has_hair):
        super().__init__(name)
        self.has_hair = has_hair

class Dog(Mammal):
    def __init__(self, name, has_hair, breed):
        super().__init__(name, has_hair)
        self.breed = breed

an1=Dog("Tommy",True,"Labrador")
print(an1.breed, an1.has_hair)


#Example2
class Device:
    def __init__(self, device_type):
        self.device_type = device_type
    def print_device(self):
        print("Device Type:", self.device_type)

class Computer(Device):
    def __init__(self, device_type,processor_type):
        super().__init__(device_type)
        self.processor_type = processor_type

    def print_processor(self):
        print("Processor Type:", self.processor_type)

class Laptop(Computer):
    def __init__(self, device_type, processor_type,battery_life):
        super().__init__(device_type,processor_type)
        self.battery_life = battery_life

    def print_battery_life(self):
        print("Battery Life:", self.battery_life)

dev1=Laptop("Portable","Ryzen 5",12)
dev1.print_battery_life()
dev1.print_processor()
dev1.print_device()
print(dev1.battery_life,dev1.device_type)