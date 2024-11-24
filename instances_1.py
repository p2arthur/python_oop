class House:
    def __init__(self, price):
        self.price = price


class Backpack:
    def __init__(self, color, size):
        self.items = []
        self.color = color
        self.material = size


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.color = 'Blue'


class Rectangle:
    def __init__(self, length, width):
        self.xSize = length
        self.ySize = width
        self.color = "Blue"


class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
