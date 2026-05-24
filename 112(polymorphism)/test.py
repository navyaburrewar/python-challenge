# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print(self.name)
#         print(self.marks)
# s1=student("navya", 50)
# s2=student("Keerthi",55)
# s1.display()
# s2.display()


# class Employee:
#     def __init__(self,name,salary):
#        self.name=name
#        self.salary=salary
#     def show_details(self):
#         print(self.name)
#         print(self.salary )
# e1= Employee("neha",4000)
# e1.show_details()


# class bank:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposite(self,d_amt):
#         self.__balance=self.__balance+d_amt
#         print(self.__balance)
#     def withdraw(self,d_wd):
#         self.__balance=self.__balance-d_wd
#         print(self.__balance)
#     def show_balance(self):
#         print(self.__balance)

# b=bank(10000)
# b.deposite(5000)
# b.withdraw(5000)
# b.show_balance()        
# 
# 


# class vehicle:
#     def start(self):
#         print("vehicle started")
# class car(vehicle):
#     def drive(self):
#         print("drive the car")  

# c1=car()
# c1.start()
# c1.drive()        


# class Animla:
#     def sound(self):
#         print("animal make sound")
# class Dog(Animla):        
#     def sound(self):
#         print("dog barks")
# class Cat(Animla):
#     def sound(self):
#         print("cat: meow")        

# d1=Dog()
# d1.sound()
# c1=Cat()
# c1.sound()        

# class Test:    
#     def _init_(self):
#         print("Constructor called")

# t = Test()

# class A:
    
#     def show(self):
#         print("Class A")

# class B(A):
#     pass

# b = B()
# b.show()

# class Student:
    
#     def _init_(self, name):
#         self.name = name

# s = Student()
# print(s.name)

# # class Animal:
    
# #     def sound(self):
# #         print("Animal sound")

# # class Dog(Animal):
    
# #     def sound(self):
# #         print("Dog bark")

# # d = Dog()
# # d.sound()

# # class Test:
    
# #     def _init_(self):
# #         self.__value = 100

# # t = Test()
# # print(t.__value)


# # class Student:
# #     def __init__(self,name,marks):
# # #         self.name=name
# # #         self.marks=marks
# # #     def grade(self):
# # #         if self.marks>50:  
# # #             print("Pass") 
# # #         else:
# # # #             print("Fail")
# # # # s1=Student("navya",100)                 
# # # # s1.grade()

# # # class ATM:
# # #     def 

# # class product:
# #     def __init__(self,name,price):
# #         self.name=name
# #         self.price=price
# #     def display(self):
# #         print(self.name,self.price)

# # p1=product("book",10)        
# # p2=product("pen",13)   
# # p3=product("pencil",12)   

# # p1.display()
# # p2.display()
# # p3.display()

# from abc import ABC,abstractmethod
# class shape(ABC):

#     @abstractmethod
#     def area(self):
#         print("area")
# class circle(shape):
#     def area(self):
#         r=4
#         a_c=3.14*r*r
#         print(a_c)
# class Reactangle(shape):
#     def area(self):     
#         l=9
#         b=8
#         a_r=2*(l+b)
#         print(a_r)


# c1=circle()
# c1.area()
# r1=Reactangle()
# r1.area()        

