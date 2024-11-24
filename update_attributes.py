class Backpack:
    def __init__(self, color):
        self.items = []
        self.color = color


my_backpack = Backpack('red')

print('my backpack 1', my_backpack.items)

my_backpack.items = ['banana', 'notebook', 'pencil']
my_backpack.color = 'blue'

print('my backpack 2', my_backpack.items)

delattr(my_backpack, 'items')

print(my_backpack.items)
