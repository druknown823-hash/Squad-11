# Factorial calulation with a with while loop

num=int(input("enter number "))
factorial=1
if num<0:
    print("sorry, factorial does not exist for negative nummber ")
elif num==0:
    print("factorial of 0is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
print(f"the factorial of {num} is { factorial}")


# Factorial calulation with a with while loop

n=int(input("enter number "))
factorial=1
if n<0:
    print("sorry, factorial does not exist for negative nummber ")
elif n==0:
    print("factorial of 0is 1")
else:
    i = 1
    while i <= n:
        factorial *= i
        i += 1

    print(f"The factorial of {n} is {factorial}")



