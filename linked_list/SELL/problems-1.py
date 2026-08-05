#  creating a sigly linkde list using while loop

class Node:
    def __init__(self,num):
        self.data=num
        self.next=None

def create_SLL(arr)    :
    if not arr:
        return None

    head=Node(arr[0])
    temp=head

    i=1
    while i<len(arr):
        new_node=Node(arr[i])
        temp.next=new_node
        temp=temp.next
        i+=1
    return head






arr=[2,3,4,5,6,7,8,9]

head=create_SLL(arr)

temp=head
while temp is not None:
    print(temp.data,end="-->")
    temp=temp.next
print(None)






#======================== / print the linked list/===========


def printlinkedlist(head):
    temp=head
    while temp is not None:
        print(temp.data,end=" ")
        temp=temp.next




head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

print(printlinkedlist(head))



#============================= ✅ Count Nodes  ========================


def printlinkedlist(head):
    count=0
    temp=head
    while temp is not None:
        
        count+=1
        temp=temp.next
    print(count)



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

printlinkedlist(head)





# /=======================✅ Sum of Nodes=============================


def printlinkedlist(head):
    sum=0
    temp=head
    while temp is not None:
        
        sum+=temp.data
        
        temp=temp.next

    print(sum)    

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
printlinkedlist(head)


#=============================== ✅ Search  ===============================

class Node:
    def __init__(self,num):
        self.data=num
        self.next=None

def create_ll(arr):
    if not arr:
        return None

    head=Node(arr[0])
    temp=head

    i=1
    while i<len(arr):
        new_node=Node(arr[i])
        temp.next=new_node
        temp=temp.next
        i+=1
    return head

def spp(head,k):
    temp=head
    index=0
    while temp is not None:
        if temp.data==k:
            print(index)
            return
        temp=temp.next  
        index+=1  

    print(None)    


arr=[2,3,5,6,7,8,9]
k=8


head=create_ll(arr)
spp(head,k) 

         
# ==========================  insert at begging =======================================


        

    






        

            