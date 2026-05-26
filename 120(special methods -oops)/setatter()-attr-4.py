#  2. setattr() → Create or change attributes dynamically

# Syntax:
# setattr(object,attribute_name,value)

class person:
    def __init__(self):
        self.name ="nikki"
p1=person()
setattr(p1,"name", "choti")

print(p1.name)


#  we can also create a new attribute that 
class  person:
    pass
p1=person()

setattr(person,"city", "hyd")
print(p1.city)

## ex-3

# using both setattr and getattr  in one ode
class  marks:
    def __init__(self):
        self.ml=89
        self.ds=100

m1=marks()
setattr(m1,"krr",70)

field=input("enter the field: ")


print(getattr(m1,field))