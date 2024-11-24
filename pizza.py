class Pizza:
    price = 10

    def __init__(self):
        self.ingredients = []


peperoni_pizza = Pizza()

print(peperoni_pizza.price)


Pizza.price = 12.32
