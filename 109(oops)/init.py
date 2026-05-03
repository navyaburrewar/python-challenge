# #  pyhton__init__() method
# ## class buildin function is __int__()
# #  The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the 
# # object is being created.

# class person:
#     def __init__ (self,name,age):
#         self.name=name
#         self.age=age
# p1 =person("navya",20)
# print(p1.name)
# print(p1.age)        

# #######   Why Use __init__()?   #################
# # #Without the __init__() method, you would need to set properties manually for each object:

# class person:
#     pass
# p1=person()
# p1.name="navya"
# p1.age=20
# print(p1.name)
# print(p1.age)


# ##3 using __init__()

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("navya",20)
# print(p1.name)
# print(p1.age)        



### default values
class student:
  def __init__(self,name,roll=20):
    self.name =name
    self.roll=roll
p1=student("navya")
p2=student("choti",21)
print(p1.name,p1.roll)
print(p2.name,p2.roll)           


### multiple parameters

class student :
  def  __init__(self,name,rollno,rank,section):
    self.name=name
    self.rollno=rollno
    self.rank=rank
    self.section=section

A1=student("nikki",6615,10,"A") 
A2=student("CHOTI",6616,11,"A")    
A3=student("nandhu",6611,12,"A")    
A4=student("sai",6612,9,"A")    
print(A1.name,A1.rollno,A1.rank,A1.section)




## important###################################

# “__init__ is used to initialize an object when it is created. It allows us to assign properties (attributes) to the object at the time of creation.”