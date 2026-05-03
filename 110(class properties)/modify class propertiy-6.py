## modifying class properties

# When you modify a class property, it affects all objects:


class person:
    lastname="" 
    def __init__(self,firstname,age):
        self.firstname=firstname
        self.age=age
p1=person.lastname="burrewar"

p1=person("navya",20)
print(p1.lastname)
