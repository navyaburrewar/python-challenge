
# INNER ORDER TRAVESERSAL

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

n1=Node(12)
n2=Node(7)
n3=Node(9)
n4=Node(8)
n5=Node(6)
n6=Node(17)
n7=Node(16)
n8=Node(18)

root=n1
n1.left=n2
n2.left=n5
n2.right=n3
n3.left=n4
n1.right=n6
n6.left=n7
n6.right=n8

def inorder(node):
    if node is not None:
        inorder (node.left)
        print(node.data)
        inorder(node.right)
print(inorder(root))


def preorder(node):
    if node is not None:
        print(node.data,end=" ")
        preorder(node.left)
        preorder(node.right)

print(preorder(root))        



def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data)






# Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         dummy = ListNode(0)
#         dummy.next = head

#         # First pass: Find the length of the linked list
#         length = 0
#         curr = head
#         while curr:
#             length += 1
#             curr = curr.next

#         # Find the node before the one to remove
#         curr = dummy
#         for _ in range(length - n):
#             curr = curr.next

#         # Delete the nth node from the end
#         curr.next = curr.next.next

#         return dummy.next




# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         dummy = ListNode(0)
#         dummy.next = head

#         # First pass: Find the length of the linked list
#         length = 0
#         curr = head
#         while curr:
#             length += 1
#             curr = curr.next

#         # Find the node before the one to remove
#         curr = dummy
#         for _ in range(length - n):
#             curr = curr.next

#         # Delete the nth node from the end
#         curr.next = curr.next.next

#         return dummy.next




    
