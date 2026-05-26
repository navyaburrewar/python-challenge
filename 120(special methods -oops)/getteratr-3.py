# # 1. getattr() → Get an attribute dynamically

# # Used to read an attribute when its name is stored in a variable.


# #  Example 1 — generally when we know which atribute is want

# class person:
#     def __init__(self):
#         self.name="navya"
#         self.age=20

# p1=person()
# print(p1.name)


# #   ex-2  normal use of getter

# class person:
#     def __init__(self):
#         self.name="navya"
#         self.age=20
# p1=person()        

# print(getattr(p1,"name"))
# print(getattr(p1,"age"))


## main thing y we use the getter()
class person:
    def __init__(self):
        self.name="navya"
        self.age=20
p1=person()     

field=input("enter attribute: ")
print(getattr(p1,field))



"""
# Without getattr() this becomes hard

# Without getattr():

if field == "name":
    print(person.name)

elif field == "age":
    print(person.age)

# If there are 100 attributes, you need many if-elif conditions.

# getattr() avoids that.
"""