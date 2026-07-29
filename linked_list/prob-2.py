# ### create multiple nodes
# n1=10
# n2=20
# n3=30
# n4=40

# class AB:
#     def __init__(self,num):
#         self.data=num
#         self.add=None
# n1=AB(10)
# n2=AB(20)
# n3=AB(30)
# n4=AB(40)

# print(n4.add)
# print(n4.data)




## CONNECTING ADDRESS
# ### create multiple nodes
# n1=10
# n2=20
# n3=30
# n4=40

# class AB:
#     def __init__(self,num):
#         self.data=num
#         self.add=None

# n1=AB(10)
# n2=AB(20)
# n3=AB(30)
# n4=AB(40)        
# n1.add=n2
# n2.add=n3
# n3.add=n4


# print(n4.add)
# print(n4.data)



#  another method
### create multiple nodes
n1=10
n2=20
n3=30
n4=40

class AB:
    def __init__(self,num):
        self.data=num
        self.add=None

n1=AB(10)
n2=AB(20)
n3=AB(30)
n4=AB(40)  
n1.add=n2      
n1.add.add=n3
n1.add.add.add=n4



print(n3)
print(n1.add.add)
print(n1.add.add.add.data)