## Write a function that takes unlimited numbers and returns only the even numbers using *args.


def even(*numbers):
    even_no= [ ]
    for i in numbers:
        if i%2==0:
            even_no+=[i]
    return even_no
        
print(even(20,39,48,57,10))        
        