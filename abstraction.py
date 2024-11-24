from abc import ABC, abstractmethod, abstractproperty,abstractproperty

class Animal:
    @property
    @abstractmethod
    def sound(self):
        pass

    def describe(self):
        return f'{self.__class__.__name__} makes {self.sound()}'


class Dog(Animal):
    def sound(self):
        return 'Bark'

class Cat(Animal):
    def sound(self):
        return 'Meows'


dog = Dog()
cat = Cat()

print(dog.describe())
print(cat.describe())
