from dog import my_dog


class Dog:

    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            print('provide a valid age')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if isinstance(age, int):
            self.age = age

my_doge = Dog('14')


my_doge.age = 'asdasdasdads'

print(f"My dog is {my_doge.age} years old")