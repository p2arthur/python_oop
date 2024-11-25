from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    PI = 3.14

    def __init__(self, radius):
        self._radius = radius


    def area(self):
        area = self.PI*self._radius**2
        return area

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        area = self._width * self._height
        return area

class AreaCalculator:

    @staticmethod
    def area(shape:Shape):
        return shape.area()


area_calculator = AreaCalculator()

circle = Circle(32)

print(area_calculator.area(circle))