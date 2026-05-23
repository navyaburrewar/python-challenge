# 3. Encapsulation Problems

########### Problem 7 — ATM Machine #####################


# Create a class ATM.

# Rules:

# balance should be private
# methods:
# deposit()
# withdraw()
# check_balance()

# Do not allow direct access to balance.

class ATM:
    def __init__(self):
        self.__balance=10000
    def deposit(self,d_amount):
        self.__balance=self.__balance+d_amount
        print(self.__balance )
    def withdraw(self,w_amount):
        self.__balance=self.__balance-w_amount
        print(self.__balance)               
    def check_balance(self):
        print(self.__balance)

a1=ATM()
a1.deposit(5000)
a1.withdraw(2500)
a1.check_balance()
