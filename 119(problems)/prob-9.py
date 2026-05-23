# Problem 9 — Marks Validation

# Create a class Student.

# Conditions:

# marks cannot be negative
# use setter and getter methods

class student:
    def __init__(self,marks):
        self.__marks=marks
    def set(self,new_marks): 
        if new_marks>=0:
            self.__marks=new_marks
        else:
            print(" marks cannot be negative")    
    def get(self):
        print(self.__marks)
s1=student(90)
s1.set(-100)
# s1.set(40)
s1.get()
