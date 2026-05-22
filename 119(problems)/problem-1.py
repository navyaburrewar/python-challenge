# # ###### classs and object basic
# Problem 1 — Student Class

# Create a class Student with:

# attributes: name, marks
# method: display()

# Create 3 student objects and print their details.



class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("student_name :",self.name)   
        print("student_marks :",self.marks) 
p1=student("navya",90)
p2=student("keerthi",95)     
p3=student("nikki",91)

p1.display()
p2.display()
p3.display()







        
        
        
        