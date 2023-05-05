"""This program aims to apply abstraction concept in oop, by creating abstract class (Shap) that have an abstract
method called area(), then two subclasses to implement that method"""
import abc
import math


class Shap(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass


class Rectangle(Shap):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width


class Circle(Shap):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi


# create instances of Rectangle and Circle
rectangle = Rectangle(10, 5)
circle = Circle(7)

# calculate area of rectangle and circle
print(f"Area of rectangle: {rectangle.area()}")
print(f"Area of circle: {circle.area()}")
