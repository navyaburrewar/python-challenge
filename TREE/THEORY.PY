# TREES

# NON-LINER DATA STRUTURE
# it is av collection node ,one node conncet multiple nodes

# types  of tress
# 1. tree         ---> no limit for node connection
# 2.binary tree(BT)  ---> the max no.of nodes can connect is 2  nodes may 0,1,2
# 3.binary search tree(bst)  --->limitr 2 nodes but nodes are in sorted
# 4.AVL TREE       -->self balanced treee
# 5. heap tree
# 6. red-block tree


class Node:
    def __init__(self,num):
        self.data = num
        self.left = None
        self.right = None
n1 = Node(1)
n2 = Node(3)
n3 = Node(2)
n4 = Node(5)
n5 = Node(4)
root = n1
n1.right = n2
n1.left = n3
n1.left.right = n4
n1.left.left = n5
root = n1
print(root.data)
print(root.left.left.data)