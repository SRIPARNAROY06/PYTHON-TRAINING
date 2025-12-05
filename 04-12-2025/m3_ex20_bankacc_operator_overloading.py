
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def __add__(self, other):
        # Assume other is also a BankAccount
        return self.balance + other.balance

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"


# ---- Example Usage ----
if __name__ == "__main__":
       acc1 = BankAccount("Asha", 1500)
       acc2 = BankAccount("Ravi", 2200)
       total = acc1 + acc2
       print(total)
