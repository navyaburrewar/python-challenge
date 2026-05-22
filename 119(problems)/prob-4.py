# # 2. Constructor (__init__) Problems#################33

#################3 Problem 4 — Employee Details##########3

# Create an Employee class using constructor to initialize:

# id
# name
# salary

# Add a method to display details.

class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print("emp_id:",self.id)
        print("emp_name :",self.name)   
        print("empt_marks :",self.salary) 
p1=Employee("6615","navya",900000)


p1.display()
 