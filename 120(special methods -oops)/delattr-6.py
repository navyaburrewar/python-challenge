# 4. delattr() → Delete an attribute dynamically
# delattr(object, attribute_name)

class Person:
    def __init__(self):
        self.name = "John"
        self.age = 30

person = Person()

delattr(person, "age")

print(hasattr(person, "age"))



#   dynamic deletion..  

class Person:
    def __init__(self):
        self.name = "John"
        self.age = 30

person = Person()

field = input("Enter attribute to delete: ")

if hasattr(person, field):
    delattr(person, field)
    print("Deleted")
else:
    print("Attribute not found")