num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
num3 = float(input("Enter the third number: ")) 

# Check if the first number is greater than BOTH the second and third
if (num1 >= num2) and (num1 >= num3): 
    # If it is, then num1 is the largest
    largest = num1 
    
# Otherwise, check if the second number is greater than the third
elif (num2 >= num1) and (num2 >= num3): 
    # If it is, then num2 is the largest
    largest = num2 
    
# If neither of the first two conditions were true, the third number must be the largest
else: 
    # If we get here, num3 is the largest
    largest = num3 

# Show the user which number was the largest
print(f"The largest number is: {largest}")