# 4. Inheritance Problems



################## Problem 10 — Vehicle Inheritance #############################3

# Create parent class Vehicle.

# Methods:

# start()

# Create child classes:

# Car
# Bike

# Both should inherit start().

class vehicle:
    def start(self):
        print("vehicles will start")
class car(vehicle):
    def c_start(self):    
        print("car will start")
class bike(vehicle):
     def b_start(self):
         print("bike  will start")
           
v1=car()
v1.start()
v2=bike()
v2.start()
