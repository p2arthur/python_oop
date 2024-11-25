from abc import ABC, abstractmethod

class Bird(ABC):
    @property
    @abstractmethod
    def fly(self):
        pass

class FlyingBird(Bird):

    @property
    def fly(self):
        return 'I can fly'

class NonFlyingBird(Bird):

    @property
    def fly(self):
        return 'I cant fly'


class Penguin(NonFlyingBird):
    pass

class Eagle(FlyingBird):
    pass


penguin = Penguin()
eagle = Eagle()

print(penguin.fly)
print(eagle.fly)