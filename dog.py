class Dog:
    def __init__(self, name):
        self._name = name


    def get_name(self):
        return self._name

    def set_name(self,new_name:str)->str:
        if isinstance(new_name, str) and new_name.isalpha() :
            self._name = new_name
        else:
            print('please enter a valid name')



my_dog = Dog("Tutuca")


dog_name = my_dog.get_name()

print(dog_name)

my_dog.set_name("Danna")

dog_name = my_dog.get_name()

print(dog_name)


class Backpack:
    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items

    def set_items(self, items:list):
        if isinstance(items, list):
            self._items = items
        else:
            print('Provide a valid items list')