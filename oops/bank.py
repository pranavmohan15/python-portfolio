class Bank:
    def __init__(self,name,ac_number):
        self.name1=name
        self.ac=ac_number
        self.balance=0

        print("ACCOUNT DETAILS")
        print("-----------------")
        print("Account Holder:",self.name1)
        print("Account Number:",self.ac)

    def deposit(self,amount):
        self.amount1=amount
        self.balance+=self.amount1
        print("Deposit completed successfully")
    
    def withdraw(self,amount):
        self.amount=amount
        self.balance-=self.amount
        if self.amount<self.balance:
           print("Withdrawal completed successfully")
        else:
            print("Insufficient Balance")
    def viewbalance(self):
        print("Balance Amount:",self.balance)
    

    
n=input("ENTER THE BANKHOLDERS NAME:")
ac=int(input("ENTER YOUR ACCOUNT NUMBER:"))
obj=Bank(n,ac)

print("1.DEPOSIT MONEY")
print("2.WITHDRAW MONEY")
print("3.VIEW BALANCE")
print("4.INVALID")

while(True):
    choice=int(input("Enter The Choice: "))
    if choice==1:
        dp=int(input("Enter the amount to deposit:"))
        obj.deposit(dp)
    elif choice==2:
        wp=int(input("Enter the withdrawal amount:"))
        obj.withdraw(wp)
    elif choice==3:
        obj.viewbalance()
    elif choice==4:
        print("CHOICE EXIT")
        break
    else:
        print("INVALID CHOICE!")
        
        



        