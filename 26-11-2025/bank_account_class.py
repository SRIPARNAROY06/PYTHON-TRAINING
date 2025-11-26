class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance =self.balance+amount

    def withdraw(self, amount):
        self.balance = self.balance-amount

    def check_balance(self):
        print(self.balance)

a1=BankAccount("SRI", 10000)
a1.deposit(50000)
a1.check_balance()
a1.withdraw(10000)
a1.check_balance()
