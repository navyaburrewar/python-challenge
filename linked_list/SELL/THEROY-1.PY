class node:
    def __init__(self,num):
        self.data=num
        self.next=None

class SELL:
    def __init__(self):
        self.head=None
    def add_end(self,num):
        new=node(num)
        if self.head==None:
            self.head=new
            self.head.next=new
        else:
            tc=self.head
            while tc.next!=self.head:
                tc=tc.next
            tc.next=new
            new.next=self.head

    def pell(self):
        if self.head ==None:
            print("we cannot add this")
        else:
            temp=self.head
            while temp.next!=self.head:
                print(temp.data,end="-->")
                temp=temp.next
            print(temp.data,"-->connects to the first node")
s=SELL()
s.add_end(20)
s.add_end(30)
s.pell()
            
    
      


                    