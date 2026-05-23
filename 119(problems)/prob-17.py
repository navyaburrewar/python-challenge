# Problem 17 — Payment Gateway

# Abstract class:

# PaymentGateway

# Abstract method:

# payment()

# Child classes:

# GooglePay
# PhonePe
# Paytm

from abc import ABC , abstractmethod
class paymentGateway(ABC):
    @abstractmethod
    def payment(self):
        pass
class googlepay(paymentGateway):
    def payment(self):
        print("google payment")
class phonepay(paymentGateway):
    def payment(self):
        print("phonepay payment")
class paytm(paymentGateway):
    def payment(self):
        print("transport through paytm")
g1=googlepay()
p1=phonepay()
pa1=paytm()

g1.payment()
p1.payment()
pa1.payment()


