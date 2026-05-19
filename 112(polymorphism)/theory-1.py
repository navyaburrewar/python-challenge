# polymorphism
#Same method name behaves differently for different objects.
#Can be method overloading or method overriding.
# create a parent class animal having sound as a method, child class dog having as a method
#  -- method overriding having same method but behave differently depend on object


class animal:
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound(self):
        print("dog sounds bow bow")        

a=animal()
a.sound()
d=dog()
d.sound()
       



### 2
# # p-employ, ch- developer, ch- manager classes---work method
class employee:
    def work(self):
        print("im employee")
class developer(employee):
    def work(self):
        print("works on code")
class manager(employee):
    def work(self):
        print("manages team")
ma=manager()
e=employee()
d=developer()
ma.work()
e.work()
d.work()            




# prob-3

#p-payment, ch-upi, ch-card---method=pay(self, amnt)

class payment:
    def pay(self, amount):
        print("payment processing")
class upi(payment):
    def pay(self, amount):
        print("paid by upi", amount)
class card(payment):
    def pay(self, amount):
        print("paid by card", amount)
c=card()
u=upi()
p=payment()
p.pay(500)
c.pay(5000)
u.pay(1000)        



## prob-4.py

#Create a base class Animal.Subclasses:
# Dog Cat Each class should implement: sound method()
# Expected:Dog → "Bark"Cat → "Meow"

class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("dog  barks")
class cat(animal):
    def sound(self):
        print("meow")         

a=animal()
a.sound()
d=dog()
d.sound()
c=cat()
c.sound()               



