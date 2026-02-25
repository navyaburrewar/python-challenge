##  Write a function that takes unlimited numbers and returns only the even numbers using *args.

def unlimited(*numbers):
    even =[]
    for num  in numbers:
        if num%2==0:
            even.append(num)
    return even
print(unlimited(21,39,48,59,10,39,78))       
