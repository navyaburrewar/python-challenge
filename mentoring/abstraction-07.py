# Shape Area (Basic)
# Create an abstract class Shape
# Method:
# area()
# Create child classes:
# Circle
# Rectangle
# Each should implement area().

from abc import ABC ,abstractmethod

class shape:
    @abstractmethod
    def area(self):
        print("40 acars of land")

class circle(shape):
    def area(self):
        print("40 acars of land")
           
class Rectangle(shape):
    def area(self):
        print("40 acars of land")

c1=circle()
c1.area()
c2=Rectangle()
c2.area()


# 2. Vehicle System
# Create abstract class Vehicle
# Method:
# start()
# Create child classes:
# Car
# Bike

from abc import ABC ,abstractmethod

class Vehicles:
    @abstractmethod
    def start(self):
        print("starting the car")

class car:
    def start(self):
        print("starting the car")

class bike:
    def start(self):
        print("starting the car")


c1=car()
c1.start()
c2=bike()
c2.start()
        
       
