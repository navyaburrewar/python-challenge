####333333 delete properties
# You can delete properties from objects using the del keyword:

class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

p1=car("bmw",2005)

del p1.model
print(p1.brand)
# print(p1.model)   ---> this line will caues the errors because we are deleted this line
