a=50
b=0
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("value is invalid")
else:
    print("division is successfull")

finally:
    print("Execution completed.")
