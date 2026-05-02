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


