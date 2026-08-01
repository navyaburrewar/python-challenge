# Head
#                     │
#                     ▼

#         n1                     n2                     n3

# +------+------+------+   +------+------+------+   +------+------+------+
# | Prev | Data | Next |   | Prev | Data | Next |   | Prev | Data | Next |
# +------+------+------+   +------+------+------+   +------+------+------+
# | None |  10  |  n2  |◄─►|  n1  |  20  |  n3  |◄─►|  n2  |  30  | None |
# +------+------+------+   +------+------+------+   +------+------+------+




class Node:
     def __init__(self,num):
        self.data=num
        self.next=None
        self.prev=None

n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)


n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3


print(n1.data)
print(n1.next)
print(n1.prev)
print(n4.next)

# adding new node at the end

class DLL:
    def __init__(self):
        self.head=None
    def add_end(self,num):
        new=Node(num)
        if self.head==None:
            self.head=new
        else:
            tc=self.head
            while tc.next!=None:
                tc=tc.next
            tc.next=new    
            new.prev=tc
    def PDLL(self):
        if self.head==None:
            print("NO Data")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end="<-->")
                temp=temp.next

    def add_begin(self,num) :
        new=Node(num) 
        if self.head==None:
            self.head=new
            
        else:
            new.next=self.head
            self.head=new
    def del_begin(self):
        if self.head==None:
            print("we cannot delete")
        else:
            self.head=self.head.next
            if self.head is not None:
                self.head.prev=None

    def del_end(self):
        if self.head==None:
            print("we cannot delete")
        elif self.head.next==None:
            self.head=None
        else:
            tc=self.head
            while tc.next.next is not None:
                tc=tc.next
            delelt= tc.next
            tc.next=None
            delelt.prev=None

    def insert_pos(self,data,pos) :
        new=Node(data)
        if self.head==None or pos==0: 
            new.next=self.head
            self.head.prev=new
        else:
            c=0
            pos=pos-1
            tc=self.head
            while pos!=c  and tc.next!=None:
                tc=tc.next
                c+=1
            new.prev=tc
            new.next=tc.next
            tc.next=new
            
    def delete_pos(self,data,pos):
        if self.head==None:
            print("we cant delete")
        elif pos==0:
            temp=self.head
            self.head=self.head.next
            if self.head.next is not None:
                


                   
             
                 
                

            


           





S=DLL()
S.add_end(30)
S.add_end(40)
S.add_end(30)
S.add_begin(411)
S.del_begin()
S.del_end()
S.insert_pos(35,3)

S.PDLL()


               

            

        
                



