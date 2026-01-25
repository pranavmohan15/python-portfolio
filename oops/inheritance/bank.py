class Bank:
    def __init__(self):
        self.__balance=0
    
    def get_bal(self):
        return self.__balance

        
class Customer(Bank):
    def deposit(self,amount):
        self.bank_balance=self.get_bal()+amount

amount=int(input("enter your deposit money:"))

obj=Customer()
obj.deposit(amount)
print("bank balance",obj.bank_balance)

