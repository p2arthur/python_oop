from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def method(self):
        print('nice method fella')

class ImplementedClass(Interface):
    def method(self):
        print("Implemented method")

class NotImplementedClass:
    def fodase(self):
        pass


def process_interface(obj:Interface):
    obj.method()


good_obj = ImplementedClass()
bad_obj = NotImplementedClass()

process_interface(good_obj)
