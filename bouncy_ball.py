# class BouncyBall:
#
#     def __init__(self, price, size, brand):
#         self._price = price
#         self._size = size
#         self._brand = brand
#
#     def get_price(self):
#         return self._price
#
#     def get_size(self):
#         return self._size
#
#     def get_brand(self):
#         return self._brand
#
#     def set_price(self, new_price):
#         self._price = new_price
#
#     def set_size(self, new_size):
#         self._price = new_size
#
#     def set_brand(self, new_brand):
#         self._price = new_brand
#
#     price = property(get_price, set_price)
#     size = property(get_size, set_size)
#     brand = property(get_brand, set_brand)
#
# my_ball = BouncyBall(32, 32,32)
#
# print(my_ball.price)


class BouncyBall:
    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        return self._price
    @property
    def size(self):
        return self._size
    @property
    def brand(self):
        return self._brand

    @price.setter
    def price(self, new_price):
        self._price = new_price
    @size.setter
    def size(self, new_size):
        self._size = new_size
    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    def bounce(self, meters):
        print(self._brand)
        print(f'Bouncing {meters} meters')


my_ball = BouncyBall(32,32,'Topper')

print(my_ball.price)

my_ball.price = 64


my_ball.bounce(13)

print(my_ball.price)