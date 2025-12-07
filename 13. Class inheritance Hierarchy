# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Animals make sounds"

# Derived class 1
class Dog(Animal):
    def sound(self):
        return "Dog barks"

# Derived class 2
class Cat(Animal):
    def sound(self):
        return "Cat meows"


# Creating objects
animal = Animal("Generic Animal")
dog = Dog("Bruno")
cat = Cat("Kitty")

# Accessing base class attributes & methods
print("Base Class:")
print("Name:", animal.name)
print("Sound:", animal.sound())

print("\nDerived Class 1 (Dog):")
print("Name:", dog.name)
print("Sound:", dog.sound())   # overridden method

print("\nDerived Class 2 (Cat):")
print("Name:", cat.name)
print("Sound:", cat.sound())   # overridden method
