class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Deposited:",amount)

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print("Withdraw:",amount)

    def get_balance(self):
        print(self.balance,"total Balance")
        print( self.name)
# Example usage:
account=bankaccount("Alice",1000)
account.deposit(int(input("Enter deposit amount:")))
account.withdraw(int(input("Enter withdrawal amount:")))
print("Current Balance:",account.get_balance())
 

