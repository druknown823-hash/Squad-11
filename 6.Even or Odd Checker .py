# Ask the user for a whole number (integer)
number = int(input("Enter a whole number: ")) 

# If a number divided by 2 has a remainder of 0, it is even.
if number % 2 == 0: 
    # If the remainder is 0, print that the number is even
    print(f"The number {number} is Even.") 
    
# If the remainder is not 0 (meaning it's 1 for a whole number), it is odd
else: 
    # Otherwise, print that the number is odd
    print(f"The number {number} is Odd.")