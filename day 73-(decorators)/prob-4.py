
# print("Function finished!")



# # Write a decorator that prints:  Function is finished...

def function(func):
    def inner():
        result = func()
        print("function is ending")
        return result
    
    
    return inner

@function
def my_func():
    print( "navya")
my_func()


