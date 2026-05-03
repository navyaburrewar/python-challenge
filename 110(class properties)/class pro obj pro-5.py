#  class properties vs object properties


# Properties defined inside __init__() belong to each object (instance properties).
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:


class person:
    species = "human"

    def __init__(self,name):
        self.name=name
p1 =person("navya")
p2=person("nikki")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)