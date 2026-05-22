##3 enccapsulation #####

# 1. Student Marks System (Basic)

# Create a class Student:
# Private variable: __marks
# Method set_marks(marks) → set marks only if between 0 and 100
# Method get_marks() → return marks

# Example Output

# Python
# s = Student()
# s.set_marks(85)
# print(s.get_marks())
# Output:
# Python
# 85



class student:
    def __init__(self):
        self.__marks=0
    def set_marks(self,marks):
        if 0<marks<100:
             self.__marks=marks
    def get_marks(self):
            return self.__marks 

s=student()
s.set_marks(85)
print(s.get_marks())    




#################  ex-2  ################

# 2. Bank Account (Basic)

# Create a class BankAccount:
# Private variable: __balance
# Method deposit(amount)
# Method withdraw(amount)
# Method get_balance()
# Rules:
# Cannot withdraw more than balance
# Deposit amount must be positive

# Example

# Python
# b = BankAccount()
# b.deposit(5000)
# b.withdraw(2000)
# print(b.get_balance())
# Output:
# Python
# 3000



class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposite(self,dep_amount):
        if  dep_amount >0:
            self.__balance+=dep_amount
        else:
            print("Deposit amount must be positive")
    def withdraw(self,wd_amount):
        if wd_amount > self.__balance:
            print("Cannot withdraw more than balance")
        else:
            self.__balance-=wd_amount    
    def get_balance(self):
            return self.__balance
b = BankAccount()
b.deposite(-5000)
b.withdraw(11000)
print(b.get_balance())
                 
                   
          



##############  ex-3   ########################




# 3. Employee Salary Management

# Create a class Employee:
# Private variable: __salary
# Method set_salary(salary)
# # Condition:
# Salary cannot be negative
# Methods:
# get_salary()

# Example
# Python
# e = Employee()
# e.set_salary(50000)
# print(e.get_salary())
# Output:
# Python
# 50000

class Employee:
    def __init__(self):
        self.__salary=0
    def set_salary(self,salary):
        if salary <0:
            print("Salary cannot be negative")
        else:
            self.__salary =salary       
    def get_salary(self):
            return self.__salary        
e=Employee()
e.set_salary(50000)
print(e.get_salary())






############ ex-4 ################




# 4. Mobile Phone Lock System

# Create a class Mobile:
# Private variable: __password
# Method set_password(password)
# Method check_password(password)
# Behavior:
# If password matches → "Phone Unlocked"
# Else → "Wrong Password"


# Example:
# Python
# m = Mobile()
# m.set_password("1234")
# print(m.check_password("1234"))
# print(m.check_password("5678"))
# Output:
# Python
# Phone Unlocked
# Wrong Password

class Mobile:
    def __init__(self):
        self.__password=0
    def set_password(self,new_password):
        self.__password=new_password

    def check_password(self,password):
        if password==self.__password:
            print("Phone Unlocked")  
        else:
            print( "Wrong Password")    
    
             

m=Mobile()
m.set_password("1234")
m.check_password("1243")
m.check_password("1234")   