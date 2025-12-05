class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner     #public
        self.__balance = balance   #private attribute

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

acc=BankAccount("Shiraan",5000)
acc.deposit(2000)
print(acc.get_balance())

acc.withdraw(3000)
print(acc.get_balance())

acc.__balance=10000  #this will not modify
print(acc.get_balance())
print(dir(acc))