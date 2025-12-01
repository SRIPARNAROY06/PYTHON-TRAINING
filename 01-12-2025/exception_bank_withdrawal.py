class LowBalanceError(Exception):
    pass

def withdraw(amount,balance):
    if amount>balance:
        raise LowBalanceError("Insufficient Balance")
    return balance-amount

check=withdraw(1000,100)
print(check)