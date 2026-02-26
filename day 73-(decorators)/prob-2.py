## Write a decorator that converts the return value of a function to uppercase.


def function(func):
    def inner():
        return func().upper()
    return inner
@function
def my_name():
    return "navyaburrewar"
print(my_name())



