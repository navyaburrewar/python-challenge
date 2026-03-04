## Write a generator function that flattens a nested list.
# Example:
# Input: [1, [2, 3], [4, [5, 6]]]
# Output: 1 2 3 4 5 6


def flattend(m):
    for i in m:
        if isinstance(i,list):
           yield from flattend(i)
        else:   
       
           yield i

for num in flattend([1,[5,7],[8,5,6]])  :
     print(num)       
