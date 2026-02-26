## 5
# Write a decorator that multiplies the function’s return value by 2.

# Example:

# get_number() → 5
# Output → 10



def function(func):
    def inner():
        result =func()*2
        return result
    return inner

@function
def my_func():
    return 78
print(my_func())


