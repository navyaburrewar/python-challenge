## Write a generator function that takes a list and yields each element one by one.

def function(list):
    for i in list:
        yield i
list =[1,2,3,4,5,6,7,8]        
for i  in function(list):
    print(i)
