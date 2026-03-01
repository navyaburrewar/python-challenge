# Use reduce() and lambda to find the maximum number in a list.
# (Hint: from functools import reduce)

from functools import reduce

num =[2,3,4,5,6,91,9]
max = reduce(lambda a,b :a if a>b else b,num)
print(max)