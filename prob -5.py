# Write a function that checks if a specific key exists in **kwargs.

def function(numb, **nums):
    return numb in nums
print(function("number",age=30, marks=29,number= 20,))    

def function(check_key, **nums):
    return check_key in nums

print(function("number", age=30, marks=29, number=20))