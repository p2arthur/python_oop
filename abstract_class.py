from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,color):
        self._color = color

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def get_info(self):
        print(f'{self.__class__.__name__} has the color {self._color}')


class Circle(Shape):

    PI = 3.14

    def __init__(self, radius, color):
        super().__init__(color)
        self._radius = radius

    def get_area(self):
        print(f'The area pf the circle is {self.PI * self._radius ** 2}')

    def get_perimeter(self):
        print(f'THe perimeter of a circle')


class Square(Shape):
    def __init__(self, width, height,color):
        super().__init__(color)
        self._width = width
        self._height = height

    def get_area(self):
        print(f'The area of the rectangle is {self._width*self._height}')

    def get_perimeter(self):
        print('perimeter of a square')


square = Square(32, 32, 'blue')
circle = Circle(32, 'purple')

square.get_area()
circle.get_area()



