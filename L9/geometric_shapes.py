import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasa trebuie să implementeze această metodă.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def __str__(self):
        return f"Circle with radius {self.radius} has area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area():.2f}"

circle = Circle(5)
rectangle = Rectangle(10, 4)
print(circle)
print(rectangle)
