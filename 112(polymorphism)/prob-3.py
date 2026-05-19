#Base class:Vehicle 
# Subclasses:Bike Car, Bus, Each vehicle:calculates rent differently, displays vehicle type. Use method overriding.
class vehicle:
    def __init__(self, rent, type):
        self.rent=rent
        self.type=type
    def calculate_rent(self):
        print("velhicle rent",self.rent)
class car(vehicle):
    def calculate_rent(self):
        total=self.rent + 100
        print(self.type,"rent:", total)
class bus(vehicle):
    def calculate_rent(self):
        total=self.rent+200
        print(self.type,"rent:",total)

class bike(vehicle):
    def calculate_rent(self):
        total=self.rent+300
        print(self.type,"rent:",total)
c=car(5000, "car")
b1=bike(2500, "bike")
b=bus(6000, "bus")
c.calculate_rent()
b1.calculate_rent()
b.calculate_rent()