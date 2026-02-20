from abc import ABC
import math

# Base class
class Shape(ABC):
    def calculate_area(self, **kwargs):
        """Calculate area based on shape type. Subclasses pass parameters via super()."""
        if 'length' in kwargs and 'width' in kwargs:
            # Rectangle
            return kwargs['length'] * kwargs['width']
        elif 'side' in kwargs:
            # Square
            return kwargs['side'] ** 2
        elif 'radius' in kwargs and 'height' in kwargs:
            # Cylinder surface area
            r = kwargs['radius']
            h = kwargs['height']
            return 2 * math.pi * r * (r + h)
        elif 'radius' in kwargs:
            # Circle
            return math.pi * kwargs['radius'] ** 2
        else:
            raise ValueError("Invalid parameters for shape")

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return super().calculate_area(length=self.length, width=self.width)

# Square subclass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return super().calculate_area(side=self.side)

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return super().calculate_area(radius=self.radius)

# Cylinder subclass
class Cylinder(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def calculate_area(self):
        return super().calculate_area(radius=self.radius, height=self.height)

# Testing
r = Rectangle(5, 3)
s = Square(4)
c = Circle(3)
cy = Cylinder(2, 5)

print("Rectangle area:", r.calculate_area())
print("Square area:", s.calculate_area())
print("Circle area:", c.calculate_area())
print("Cylinder area:", cy.calculate_area())
