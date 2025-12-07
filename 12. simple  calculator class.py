class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
#if __name__ == "__main__":
    #calc = Calculator()
    #print("Addition:", calc.add(10, 5))
    #print("Subtraction:", calc.subtract(10, 5))
    #print("Multiplication:", calc.multiply(10, 5))
    #print("Division:", calc.divide(10, 5))
    #try:
       #print("Division by zero:", calc.divide(10, 0))
    #except ValueError as e:
        #print(e)

calc = Calculator()
num1=float(input("enter first number"))
num2=float(input("enter second number"))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    print("Result:", calc.add(num1, num2))
elif operation == '-':
    print("Result:", calc.subtract(num1, num2))
elif operation == '*':
    print("Result:", calc.multiply(num1, num2))
elif operation == '/':
    try:
        print("Result:", calc.divide(num1, num2))
    except ValueError as e:
        print(e)
        


