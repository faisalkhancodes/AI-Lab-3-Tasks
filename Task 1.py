from abc import ABC, abstractmethod
import math

# Base class
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width

# Square class
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        return self.side ** 2

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius ** 2

# Cylinder class
class Cylinder(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def calculate_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

# Testing
r = Rectangle(5, 3)
s = Square(4)
c = Circle(3)
cy = Cylinder(2, 5)

print("Rectangle area:", r.calculate_area())
print("Square area:", s.calculate_area())
print("Circle area:", c.calculate_area())
print("Cylinder area:", cy.calculate_area())