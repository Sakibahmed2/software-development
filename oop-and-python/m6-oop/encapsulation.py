class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name
        self.__balance = initial_deposit
        self._branch = 'Baniyachong'

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return f'Fokir tor taka nai {self.__balance}'


sakib = Bank("Sakib", 20000)
sakib.deposit(100)

print(sakib.get_balance())
print(sakib._branch)
print(sakib.withdraw(200))
print(dir(sakib))
print(sakib._Bank__balance)