# Write a generator function that yields cumulative sums of a list.
# Example:
# Input: [1, 2, 3, 4]
# Output: 1, 3, 6, 10



def func(m):
    sum =0
    for i in m:
       sum+=i
       yield sum

for n in func([1,2,3,4]):
    print(n)






