# BST (binary search tree)

# no duplicates
# data stores  in the sorted manner
# --> if root is none
    # -->create node adn make it root
# --> if samll add at left
# -->greatest add to right


"""
          17
         /  \
       15    19
      /        \
    11          25
   /           /  \
  7          23   29
"""


[19,24,11,13,7,9,8,26,32,64,31,72,16]

# 3  method to print the bse on the  output
#  3 types of traversal methods
# 1.inner order
# 2.pre -order
# 3.post-order

#========================== basic recursion========================= 
# 
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=5
print(fact(n))