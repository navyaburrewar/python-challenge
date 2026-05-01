## Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.



## creating a class
# To create a class, use the keyword class:


############       3 ex-1   ########################
# Create a class named MyClass, with a property named x:

class myname:
    maeks=20
print(myname)    



################### creating an obj ################3
# Now we can use the class named MyClass to create objects:
class myname:
    marks=20
obj=myname()
print(obj.marks)    



#################### del obj ###############
# class marks:
#     ml=20
# p1=marks()
# del p1
# print(p1) 
## output: NameError: name 'p1' is not defined


#### multiple objects ##############

class marks:
    ml=30
p1 = marks()
p2 = marks()
p3 =marks()

print(p1.ml)
print(p2.ml)
print(p3.ml)

 

 ### the pass statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class person:
    pass