"""creating shap class with  a method area() that returns the area of the shape. Then create two subclasses Rectangle
and Circle that override the area() method to return the area of the corresponding shape. Create a function
get_shape_area(shape) that takes a shape object as input and returns its area."""
import math


class Shap:
    def area(self):
        pass


class Rectangle(Shap):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shap):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


def get_shap_area(shap):
    return shap.area()


rectangle = Rectangle(4, 5)
circle = Circle(3)
print(get_shap_area(rectangle))
print(get_shap_area(circle))
