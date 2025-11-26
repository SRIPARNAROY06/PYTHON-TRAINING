class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2

    def multiply(self):
        return self.num1*self.num2

    def divide(self):
      try:
          return self.num1/self.num2
      except ZeroDivisionError:
          return "Cannot divide by zero"



a1 = Calculator(10,0)
print(a1.add())
print(a1.sub())
print(a1.multiply())
print(a1.divide())



