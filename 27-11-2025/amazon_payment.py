class Payment:
    def pay(self,amount,balance):
        print("Payment Amount:",amount)
        print(f"Remaining balance:{balance}")
        return balance

class Gpay(Payment):
    def pay(self, amount, balance):
        balance -= amount
        print(f"{amount} paid successfully")
        print(f"Remaining balance:{balance}")
        return balance

class Paytm(Payment):
    def pay(self, amount, balance):
        balance -= amount
        print(f"{amount} paid successfully")
        print(f"Remaining balance:{balance}")
        return balance

class PhonePay(Payment):
    def pay(self, amount, balance):
        balance -= amount
        print(f"{amount} paid successfully")
        print(f"Remaining balance:{balance}")
        return balance

def main():
    print("Welcome to the Payment App")
    try:
        balance=float(input("Enter your Balance:"))
        amount=float(input("Enter your Amount:"))
    except ValueError:
        print("Invalid Input")
        return

    if amount > balance:
        print("Insufficient Balance")
        return
    else:
        print("Current Balance is sufficient:",balance)

    print("Choose Payment Mode: ")
    print("1.GPay")
    print("2.PhonePay")
    print("3.Paytm")

    choice=int(input("Enter your Choice:"))
    if choice==1:
        print("Payment Mode:")
        method=Gpay()

    elif choice==2:
        print("Payment Mode:")
        method=PhonePay()

    elif choice==3:
        print("Payment Mode:")
        method=Paytm()

    else:
        print("Invalid Input")
        return

    balance=method.pay(amount,balance)
    print("Payment completed")


if __name__ == "__main__":
    main()












