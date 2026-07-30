## finding the last node and creating the new node without knowing the previous node and address only by knowing the one thing onlyyy

class Node:
    def __init__(self,num):
        self.data=num
        self.add=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
n1.add=n2
n2.add=n3
n3.add=n4


head=n1
temp=head
while temp.add is not None:
    temp=temp.add
temp.add=n5 


head=n1
temp=head
while temp!=None:
    print(temp.data,end="-->")
    temp=temp.add

