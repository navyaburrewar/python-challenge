## pyhton self parameter

## here in self paramer that we can use the paramters in the function using the self that value we can use in any other places or other function by using self parameter we can access it


## ex-1
class student:
    def __init__(self,name,age):
        self.name =name
        self.age=age

    def student1(self):
        print("helo my name is " +self.name + " my age is "+self.age)   ## without using f"string here

p1=student("navya","20")
p1.student1()



##ex-2  ### same as about using f'string formate
class student:
    def __init__(self,name,age):
        self.name =name
        self.age=age

    def student1(self):
        print(f"helo my name is  {self.name} my age is {self.age}")   ## without using f"string here

p1=student("navya",20)
p1.student1()



# self Does Not Have to Be Named "self"
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class:
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()



#  Calling Methods with self
# You can also call other methods within the class using self:

class person:
    def __init__(self,name):
      self.name=name
    def greet(self):
       return "helo"+ self.name
    def welcome(self):
       print(self.greet()+"welcome to collage")

p1 = person("navya")
p1.welcome()         