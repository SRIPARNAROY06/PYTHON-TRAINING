def add(a: float, b: float):
    return a + b

def subtract(a: float, b: float):
    return a - b

def multiply(a: float, b: float):
    return a * b

def divide(a: float, b: float):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ").strip()
    func = ops.get(op)

    if func is None:
        print("Invalid operation selected.")
    else:
        try:
            result = func(a, b)
            print("Result:", result)
        except ZeroDivisionError as e:
            print("Error:", e)
            
