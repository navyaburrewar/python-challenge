class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"welcome{self.name} of age{self.age}")

p1=student("neha",15)
# del student.greet     if i commentout this it will the erro to me

p1.greet()


##3 output ----
## output will gives the erro value here