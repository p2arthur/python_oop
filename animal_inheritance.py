class Animal:
    def __init__(self, name):
        self._name = name


    def speak(self):
        print(f'{self._name} makes a sound')

class Dog(Animal):
    def speak(self):
        print(f'{self._name} barks')

class Cat(Animal):
    def speak(self):
        print(f'{self._name} meows')



cat = Cat('Wwiskeeeey')
dog = Dog('Toyzinho meu amor')

cat.speak()
dog.speak()