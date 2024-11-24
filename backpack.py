class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items


    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print('Please enter a valid item')

    def remove_item(self,item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            print('Item to be deleted not found')
            return 0

    def add_items(self, items_list):
        for item in items_list:
            self.add_item(item)

    def has_item(self, item):
      return item in self._items


    def sorted_items(self,is_sorted=False):
        if is_sorted:
          return sorted(self._items)
        else:
            return self._items




my_backpack = Backpack()


items = my_backpack.items

print(items)

my_backpack.add_item('banana')

print(items)


class Circle:
    PI = 3.1416

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    # Define your method below:

    def find_area(self):
        return (2 * self.PI) ** self.radius


blue_circle = Circle(15, "Blue")

# Write your code below:

area = blue_circle.find_area()
my_backpack.add_item('um chá')

print(items)

print(my_backpack.has_item('um chá'))
print(my_backpack.has_item('seda'))

my_backpack.add_item('seda')

my_backpack.add_items(['maconha', 'dichavador', 'curcuma'])

print(my_backpack.sorted_items(True))

