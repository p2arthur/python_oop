class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number =  account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self.__balance

    @account_number.setter
    def account_number(self, number):
        self._account_number = number


    def add_balance(self, amount):
        if amount > 0:
            self.__balance += amount
            return 1
        else:
            print('Deposited invalid amount')
            return 0

    def withdraw_amount(self, amount):
        if self.__balance >= amount > 0:
           self.__balance -= amount
           return 1
        else:
            print('Withdrawing invalid amount')




account = BankAccount(1234, 1000)
print(account.balance)
account.add_balance(-32)
account.add_balance(32)
print(account.balance)
account.withdraw_amount(6000)
account.withdraw_amount(732)
print(account.balance)
