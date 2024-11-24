class Car:

    def __init__(self, brand, model, year, color, driver):
        self._brand = brand
        self._model = model
        self._year = year
        self.color = color
        self.__something = 'somethings'


my_car = Car('Fiat', 'Uno', '1997', 'red', 'arthur')


something = my_car._Car__something

print(something)


class Book:

    def __init__(self, title, author, num_pages, ISBN, publisher):
        self.title = title
        self.author = author
        self._num_pages = num_pages
        self._ISBN = ISBN
        self._publisher = publisher
