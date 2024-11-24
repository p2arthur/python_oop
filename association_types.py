# Association

class Student:
    def __init__(self, name):
        self.name = name
        self.backpack = None
        print('backpack0', self.backpack)


class Backpack:
    def __init__(self):
        self.items = ['apple']


student = Student('Arthur')
backpack = Backpack()

print('Association', student, backpack)
# Reference


class Student:
    def __init__(self, name, backpack):
        self.name = name
        self.backpack = backpack
        print('backpack1', self.backpack.items)


class Backpack:
    def __init__(self):
        self.items = ['banana']


backpack = Backpack()
student = Student('Marcelo', backpack)
print('Reference', student, backpack)

# Composition


class Student:
    def __init__(self, name):
        self.name = name
        self.backpack = Backpack()
        print('backpack2', self.backpack.items)


class Backpack:
    def __init__(self):
        self.items = ['orange']


student = Student('Arthur')
print('Composition', student)
