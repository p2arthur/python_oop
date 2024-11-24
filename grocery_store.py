class CashRegister:
    def __init__(self, cashier):
        self._cashier = cashier
        self._items = []
        self._total_before_taxes = 0
        self._total_taxes = 0

    @property
    def items(self):
        return self._items
    @property
    def total_before_taxes(self):
        return self._total_before_taxes
    @property
    def total_taxes(self):
        tax = self._total_before_taxes * 0.05
        self._total_taxes = tax
        return self._total_taxes

    @property
    def total_amount(self):
        return self._total_before_taxes + self._total_taxes

    @property
    def cashier(self):
        return self._cashier

    def add_product(self,item, quantity=1):
        self._items.append(item)
        self._total_before_taxes+=item.price
        self._total_taxes = self._total_before_taxes * 0.05

    def remove_product(self,item):
        if item is self._items:
            self._items.remove(item)
            self._items-=item.price
        else:
            print('Product not registered')

    def clear_cash_register(self):
        self._items = []
        self._cashier =''
        self._total_taxes = 0
        self._total_before_taxes = 0


class Product:
    def __init__(self, name, price):
        self._price = price
        self._name = name

    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price

product1 = Product('Pizza', 10.34)
product2 = Product('Donut', 5.23)


cash_register = CashRegister('Arthur')

print(cash_register.cashier)

cash_register.add_product(product1)
cash_register.add_product(product2)

print(cash_register.total_amount)
