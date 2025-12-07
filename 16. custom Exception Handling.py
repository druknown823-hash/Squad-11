from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Derived class 1: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.1416 * self.radius


# Derived class 2: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Using the derived classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

print("\nRectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

