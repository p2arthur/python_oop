from abc import ABC, abstractmethod

class Greeting:
    def __init__(self, name):
        self._name = name

#This is the contract saying that any other cass that inherits from this will have this abstract method
    @abstractmethod
    def greet(self):
        print(f'Hello {self._name}')



class BetterGreeting(Greeting):
    def __init__(self, name):
        super().__init__(name)

    def greet(self):
        print(f'Hello {self._name} your motherfucker')



