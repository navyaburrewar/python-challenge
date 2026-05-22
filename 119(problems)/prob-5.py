################  Problem 5 — Bank Account  ###################

# Create a class BankAccount.

# Methods:

# deposit()
# withdraw()
# check_balance()

# Use constructor to initialize account holder name and balance.

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,m_deposite):
        self.balance=self.balance+m_deposite
        print("after_deposite:",self.balance)
    def withdraw(self,m_withdaw):
        self.balance= self.balance-m_withdaw
        print("after_withdraw :",self.balance)
    def check_balance(self):

        print("current_balance: ",self.balance)
b=BankAccount("nikki",100000)
b.deposit(50000)
b.withdraw(50000)
b.check_balance()



        
        
        
        