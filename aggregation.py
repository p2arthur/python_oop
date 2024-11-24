class Author:
    def __init__(self, name, birth_year):
        self._name = name
        self._birth_year = birth_year

    @property
    def name(self):
        return self._name

    @property
    def birth_year(self):
        return self._birth_year

class Book:
    def __init__(self, name, author:Author):
        self._name = name
        self._author = author
        self.words = []

        

    def get_book(self):
        print(f'{self._name} - {self._author.name}, {self._author.birth_year}')


author = Author('Stephen King', 1947)
book = Book('1408', author)


book.get_book()