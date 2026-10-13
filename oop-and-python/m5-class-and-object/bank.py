class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 1000
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw or amount > self.max_withdraw:
            print(f"Enter a valid amount minimum {self.min_withdraw} and maximum {self.max_withdraw}")
        elif amount > self.balance:
            print(f"You dont have enough money to withdraw current balance {self.balance}")
        else:
            self.balance -= amount
            print( f"Here is you new balance after withdraw {self.balance}")

ibbl = Bank(20000)

ibbl.withdraw(1000)
ibbl.withdraw(3000)
ibbl.withdraw(30000)
ibbl.deposit(20000)
ibbl.withdraw(30000)