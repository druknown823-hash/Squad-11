# Ask the user for the temperature in Fahrenheit and convert it to a number
fahrenheit = float(input("Enter temperature in Fahrenheit: ")) 

# This is the formula to convert Fahrenheit to Celsius: (F - 32) * 5/9
celsius = (fahrenheit - 32) * 5/9 

# Show the user the calculated temperature in Celsius
# We use an f-string to easily combine text and the calculated value
print(f"The temperature in Celsius is: {celsius}")