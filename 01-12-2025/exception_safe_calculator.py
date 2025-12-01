def safe_calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Error: Invalid operator. Please use +, -, *, or /.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numeric inputs.")


safe_calculator()
