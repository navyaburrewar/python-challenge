## singly linked list

class Node:
    def __init__(self,num):
        self.data=num
        self.Next=None

class SLL:
    def __init__(self):
        self.head=None

    def add_end(self,num):
        new=Node(num)    
        if self.head is None:
            self.head=new
        else:
            tc=self.head
            while tc.Next is not  None : 
                tc=tc.Next
            tc.Next=new  
    def psll(self):
        if self.head is None:
            print("no data")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end="-->")  
                temp=temp.Next
            print("temp getout from the train")             
            

T=SLL()
T.add_end(10)
T.add_end(20)
T.add_end(30)
T.psll()
T.add_end(40)
T.psll()