# Problem 1: Basic Inheritance
# Task:
# Create a class Animal with a method sound() that prints "Animal makes sound".
# Create a child class Dog that calls the same method.
# 👉 No overriding, just inheritance

class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def child(self):
       print("animal is dog")
p1=Dog() 

p1.sound()
p1.child()



# 🔹 Problem 2: Simple Method Change


# Task:
# Create a class Bird with method fly() that prints "Bird can fly".
# Create a child class Parrot that changes the message to "Parrot can fly high".
# 👉 Basic method overriding

class Bird:
    
    def fly(self):
        print("birds can fly")
class parrot(Bird):
    def fly(self):
        print("birds can fly")

        
p1=parrot()      
p1.fly() 
    



# 🔹 Problem 3: Using Attributes

# Task:
# Create a class Person with:
# name
# Create a child class Student that:
# prints "Student name is <name>"
# 👉 Focus on accessing parent data

class person:
    def c_name(self,name):
        self.name=name
        
  
class Student(person): 
    def Show(self):
        print("Student name is",self.name)
   
p1=Student()
p1.c_name("navya")
p1.Show()

############## 4  #################333


# 🔹 Problem 4: Reuse Parent Method
# Task:
# Create a class Vehicle with method start() → "Vehicle started"
# Create a child class Bike that uses the same method without changing anything.
# 👉 Understanding code reuse

class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle) :
    pass            
       
p1=Bike()
p1.start()          


## the below problem  same mehtod but the print statement different then it give the child property only
class employee:
    def work(self):
        print("get salary")
class developer(employee):
    def work(self):
        print("works hard")

p1=developer()
p1.work()
