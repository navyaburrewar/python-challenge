# 3. hasattr() → Check whether attribute exists


class Person:
    def __init__(self):
        self.name = "John"

person = Person()

print(hasattr(person, "name"))
print(hasattr(person, "age"))
print(hasattr(person,"marks"))

## it simply says that where taht attritube present are not 



##  Avoid error

class Person:
    def __init__(self):
        self.name = "John"

person = Person()

field = "age"

if hasattr(person, field):
    print(getattr(person, field))
else:
    print("Attribute not found")