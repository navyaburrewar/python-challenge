# Problem 14 — Payment System

# Parent class:

# Payment

# Child classes:

# CreditCardPayment
# UPIPayment
# CashPayment

# Each should override pay().


class payment:
    def pay(self):
        print("you can pay online")
class creditcardpayment(payment):
    def pay(self):
        print("you pay using creditcard")
class upipayment(payment):
    def pay(self):
        print("you can pay using the upipayment")
class cashpayment(payment) :
    def pay(self):
        print("you can pay using then cash") 

c1=creditcardpayment()
u1=upipayment()
c2=cashpayment()

c1.pay()
u1.pay()
c2.pay()
