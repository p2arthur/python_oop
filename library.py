class Book:
    def __init__(self, title, author, serial_number):
        self._title = title
        self._author = author
        self._serial_number = serial_number


    def print_details(self):
        print(self._title, self._author, self._serial_number)



class User:
    def __init__(self, name):
        self.name = name



book = Book('The shinning', 'Stephen king', 32)

Book.__init__(book, 'Marcola', "Arthur", 666)

class Ebook(Book):
    def __init__(self, title, author, isbn) :
        super().__init__(title, author, isbn)

ebook = Ebook('Meus ovo', "Teus ovo", 123132123)

print('ebook', ebook._title);


