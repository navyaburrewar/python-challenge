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






# / print the linked list


def printlinkedlist(head):
    temp=head
    while temp is not None:
        print(temp.data,end=" ")
        temp=temp.next




head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

print(printlinkedlist(head))



# ✅ Count Nodes
def printlinkedlist(head):
    count=0
    temp=head
    while temp is not None:
        print(temp.data,end=" ")
        count+=1
        temp=temp.next
    print(count)



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

print(printlinkedlist(head))


            