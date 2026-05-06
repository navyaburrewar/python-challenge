
# # super() key word in Inheritance-----
# # even though we are passing the parent class name into the child class , when the
# #child class contains constructor , it will only print it's own attributes and
# #properties & couldn't access the data from parent class 


# """
# class Car:
#     def __init__(self, name):
#         self.name = name
#         #self.age = age

# class red_c(Car):
#     def __init__(self, color, name):
#         super().__init__(name)
#         self.color = color

    

# c = red_c("blue", "ram")
# print(c.color, c.name)

# """



# """
# class Car:
#     def __init__(self, name):
#         self.name = name
#         #self.age = age

# class red_c(Car):
#     def details(self):
#         print("Hi my name is", self.name)

    

# c = red_c("Ram")
# c.details()

# """


# #problem on Inheritance super() keyword------------

# #initialise a parent class as Employee-constructor with parameter name, child class as Developer - constructor with parameter prog_lang, use super()
# # to get 2 parameter data



# # make a class animal - contain a method with print("animal is shouting"), make 2 child classes
# #dog - method with print "bow"& cat - method with print "meow"


# #04/06/2026
# #Abstraction --- it is the process of showing only necessary things & hiding unnecessary features
# #Example -- Car steering, break, gear and the engine working
# # using abstract method the things in the class which was attached by abstractmethod should not be called with any object
# #abstract method forces the child classes to write the same methods which are inside the parent class
# # abc - abstract base class == ABC, abstract method
# """
# class vehicle:
#     def method(self):
#         print("I'm vehicle")

# v = vehicle()
# v.method()

# """
# from abc import ABC, abstractmethod


# class Vehicle(ABC):
    
#     @abstractmethod
#     def start(self):
#         print("I'm vehicle")
        

# class Car(Vehicle):
#     """
#     def start(self):
#         print("HIIIIIIIIII")
#     """
#     def stop(self):
#         print("i will start with key")

# class Bike(Vehicle):
    
#     def start(self):
#         print("HIIIIIIIIII")
    
#     def stop(self):
#         print("i will start with key")
    
# car = Car()
# car.start()
# car.stop()
