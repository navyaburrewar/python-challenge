
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









