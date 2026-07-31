class Node:
    def __init__(self,data):
        self.data=data
        self.add=None
class sll:
        def __init__(self):
            self.head=None

        def count_nodes(self):    
            if self.head==None:
                print( "0")    
            else:
                c=0
                temp=self.head
                while temp is not None:
                    temp=temp.add
                    c+=1
                return c

n1=Node(10)
n2=Node(20)

n1.add=n2
s=sll()

s.head=n1
print(s.count_nodes())





