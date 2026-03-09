from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def circumference(self):
        return 2 * (self.width + self.height)



c = Circle(5)
r = Rectangle(10, 5)

print("Circle Area:", c.area())
print("Circle Circumference:", c.circumference())

print("Rectangle Area:", r.area())
print("Rectangle Circumference:", r.circumference())