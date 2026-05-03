# modify properties
# You can modify the value of properties on objects:

class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
p1=car("bmw",2008)
print(p1.brand) 

p1.model=2006
print(p1.model)
