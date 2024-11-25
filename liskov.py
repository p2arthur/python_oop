from abc import abstractmethod, ABC


class Vehicle(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Motorcycle(Vehicle):

    def make_sound(self):
        print('Dança da motinha')

    def do_willy(self):
        print('randandandandan é ograu caraiii')

class Car(Vehicle):

    def make_sound(self):
        print('É o camaro amarelo kraiii')

    def open_door(self):
        print('Opening the door')

class StreetCar(Car):

    def open_door(self):
        print('I can only open two doors')

class StreetMotorcycle(Motorcycle):
    def do_willy(self):
        print('I can do willy because its street')