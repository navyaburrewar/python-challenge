#   Methods Modifying Properties

class student:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def details(self) :
        self.dept="csm"
        print(f"hi {self.name} your from {self.dept}")
p1=student("neha","ece")

p1.details()