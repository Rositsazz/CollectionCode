class BankAccount:

    def __init__(self, name, balance, currency):
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(balance, int):
            raise TypeError
        if not isinstance(currency, str):
            raise TypeError
        if balance < 0:
            raise ValueError("Balance can not be under 0")

        self.__name = name
        self.__balance = balance
        self.__currency = currency
        self.__history = []
        self.__create_history("Account was created")

    def get_name(self):
        return self.__name

    def get_balance(self):
        self.__create_history("{} Balance-> {}{}".format(self.__name,
                                                         self.__balance,
                                                         self.__currency))

        return self.__balance

    def get_currency(self):
        return self.__currency

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative money")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("You can not withdraw")
            return False
        self.__balance -= amount

    def __create_history(self, event):
        self.__history.append(event)

    def get_history(self):
        return self.__history

# account = BankAccount("Rado", 0, "$")
# account.deposit(10)
# print(account.get_balance())
# account.withdraw(5)
# print(account.get_balance())
