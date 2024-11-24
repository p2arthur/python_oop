class Backpack:
    MATERIAL = 'fabric'

    def __init__(self, size, items):
        self.size = size
        self.items = items


my_backpack = Backpack('m', ['banana'])


print(my_backpack.MATERIAL)
