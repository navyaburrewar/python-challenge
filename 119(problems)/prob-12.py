# Problem 12 — Animal Sounds

# Parent class:

# Animal

# Child classes:

# Dog
# Cat
# Cow

# Each child should have its own sound() method.


class animal:
    pass
class dog(animal):
    def sound(self):
        print("dog-bow")
class cat(animal):
    def sound(self):
        print("cat-meow")
class cow(animal):
    def sound(self):
        print("cow-sound")
c1=dog()
c1.sound()
c2=cat()
c2.sound()
c3=cow()
c3.sound()        
