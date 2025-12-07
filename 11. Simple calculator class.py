ef add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide (x,y):
    if y == 0:
        return "division by 0."
    return("x/y")
print("select Opreation")
print("1.Add ")
print("2.subtract")
print("3.Multiply")
print("4.Divide")

choice=input("enter choice(1/2/3/4/):")
num1=float(input("enter first number"))
num2=float(input("enter second number"))

if choice =="1":
    print("result:",add(num1, num2))
elif choice=="2":
    print("result:",subtract(num1,num2))
elif choice=="3":
    print("result" ,multiply(num1,num2))
elif choice=="4":
    print("result:",divide(num1,num2))
else:
    print("invalid output")



