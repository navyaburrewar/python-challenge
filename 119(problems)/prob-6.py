# Problem 6 — Car Information

# Create a Car class with constructor.

# Attributes:

# company
# model
# year

# Add method car_info().


class car:
    def __init__(self,company,model,year):
        self.company=company
        self.model=model
        self.year=year
    def car_info(self):
        print("company:",self.company)
        print("model:",self.model)
        print("year:",self.year)

c1=car("shift","az",2000)
c1.car_info()        