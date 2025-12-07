# Base class
class Vehicle:
    def start(self):
        return "Vehicle is starting"

# Derived class overriding the method
class Car(Vehicle):
    def start(self):
        return "Car starts with a key"

# Creating objects
v = Vehicle()
c = Car()

# Calling methods
print("Base Class Method:", v.start())
print("Derived Class (Overridden Method):", c.start())
