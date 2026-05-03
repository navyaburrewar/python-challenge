## class methods
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def greet(self):
        print(f"heloo {self.name} rollno {self.rollno}")    
p1 =student("nandhu",30)
p1.greet()