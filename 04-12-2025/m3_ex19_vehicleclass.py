
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def max_speed(self):
        return "Max speed not specified"

    def display(self):
        print(f"Vehicle: {self.make} {self.model}, Max Speed: {self.max_speed()}")


class Car(Vehicle):
    def max_speed(self):
        return "200 km/h"  # Override for Car


class Bike(Vehicle):
    def max_speed(self):
        return "120 km/h"  # Override for Bike


## ---- Example Usage ----
if __name__ == "__main__":
    car = Car("Hyundai", "i20")
    bike = Bike("Honda", "Shine")

    car.display()
