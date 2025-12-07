# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Taking range from user
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

sum_primes = 0

# Loop through the range and sum prime numbers
for number in range(start, end + 1):
    if is_prime(number):
        sum_primes += number

print("Sum of all prime numbers in the range =", sum_primes)
