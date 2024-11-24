from abc import ABC, abstractmethod

# This is an Interface that will provide an abstract contract of methods to classes that will inherit
class Interface(ABC):
    @abstractmethod
    def method(self):
        pass

# Implementing the abstract class and overriding the parent methods
class ChildrenClass(Interface):
    def method(self):
        print('method needed from the paren abstract interface')

class SecondChildrenClass(Interface):
    def method(self):
        print("method needed from the parent abstract interface")


my_object = ChildrenClass()
my_object2 = SecondChildrenClass()

my_object.method()
my_object2.method()