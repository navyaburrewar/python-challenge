# 6. Abstraction Problems
# Problem 16 — Abstract Vehicle

# Use ABC and abstractmethod.

# Create abstract class:

# Vehicle

# Abstract methods:

# start()
# stop()

# Child classes:

# Car
# Bike

from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        print("starting the vehicle")
    @abstractmethod    
    def stop(self):
        print("stoping the vehicle")
class car(vehicle):
    def start(self):
        print("car will start")
    def stop(self):
        print("car will stop")
class bike(vehicle):
    def start(self):
        print("bike will start")
    def stop(self):
        print("bike will stop")

c1=car()
c1.start()
c1.stop()
b1=bike()
b1.start()
b1.stop()


      
                      