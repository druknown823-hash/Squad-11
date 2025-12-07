# Custom Exception Class
class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)


# Function that uses the custom exception
def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative!")
    elif age < 18:
        raise InvalidAgeError("You must be at least 18 years old.")
    else:
        print("Age is valid, access granted.")


# Main Program
try:
    age = int(input("Enter your age: "))
    check_age(age)

except InvalidAgeError as e:
    print("Custom Exception Caught:", e)

except ValueError:
    print("Please enter a valid number!")
