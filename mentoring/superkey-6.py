#initialise a parent class as Employee-constructor with parameter name, child class as Developer - constructor with parameter prog_lang, use super()
# to get 2 parameter data

class Employee:
    def __init__(self,name):
        self.name=name
class Developer(Employee):
    def __init__(self,name,prog_lang) :
        
        super().__init__(name)
        print("my name is ",self.name)
        self.prog_lang=prog_lang

p1=Developer("navya","python")  
print(p1.name)
     



# # make a class animal - contain a method with print("animal is shouting"), make 2 child classes
# #dog - method with print "bow"& cat - method with print "meow"


class animal:
    def sound(self):
        print("animal is shouting")
class dog(animal):
    def aa(self):
        print('bow')
class cat(animal):
    def bb(self):
        print("meow")

c1=dog()
c1.sound()
c2=cat()
c2.sound()


