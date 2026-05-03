### class  properties
# Properties are variables that belong to a class. They store data for each object created from the class.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("nikki",20)
print(p1.name)
print(p1.age)        