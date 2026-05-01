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
# p2.age=20

## single inheritance 

# class parent:
#     def aa(self):
#         print("elders")

# class child(parent):
#     def bb(self):
#         print("childern")  

# c1=parent()
# c2=child()
# c1.aa()
# c2.bb()



##3 multiple inheritance

class grandparent:
    def aa(self):
        print("thatha")
class dad:
    def bb(self):
        print("nana")

class child(grandparent,dad):
    def cc(self):
        print("kids")

A1= child()
A1.bb()
A1.cc()     


# ### multilevel inheritance
# class grandfather:
#     def zz(self):
#         print("older")
# class parent(grandfather):
#     def aa(self):
#         print("elders")

# class child(parent):
#     def bb(self):
#         print("childern") 

# A1=child()
# A1.aa()        



# ### hierachical inheritance

# class father:
#     def men(self):
#         print("piller of home")
# class daughter(father):
#     def girl(self):
#         print("cute girl") 
# class son (father):
#     def boy(self):
#         print("cute boy")
# A1=son()
# A1.men()          
