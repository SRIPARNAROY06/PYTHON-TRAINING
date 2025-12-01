#example1

try:
    x=10/0
except ZeroDivisionError:
    print("Cannot divide by zero")

#example2
try:
    num=int(input("Enter a number:"))
    print(10/num)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")

#example3
try:
    f=open("data.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Close the file") #memory management. something which has to be done for that we use finally

#example4
try:
    value=int("50")
except ValueError:
    print("Invalid input")
else:
    print("Conversion successful: ",value)

#example5 --manually raising an error
def check_age(age):
    if age<18:
        raise ValueError("Age must be 18 or above")
    return "Allowed Age"
print(check_age(11))

#example6--custom exception
class LowBalanceError(Exception):
    pass

def withdraw(amount,balance):
    if amount>balance:
        raise LowBalanceError("Insufficient Balance")
    return balance-amount

check=withdraw(1000,100)
print(check)