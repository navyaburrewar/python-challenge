#  methods accessing propereties

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        return f"{self.name} is{self.age} years old"
    
p1 =person("navya","29")
print(p1.greet())
 




 ## ex-2 ---> same but here not returning the values directlly printing the values
 


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"{self.name} is{self.age} years old")
    
p1 =person("navya","29")
p1.greet()