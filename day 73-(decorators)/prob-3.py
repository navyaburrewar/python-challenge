
# # Write a decorator that prints:  Function is starting...


def function(func):
    print("Function is starting...")
    def inner():
         return func().upper()
    return inner

@function
def my_name():
    return "navyaburrewar"
print(my_name())

