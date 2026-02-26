# 1️⃣ Write a Decorator to Count Function Calls

# Question:
# Write a decorator @count_calls that counts how many times a function has been called


def function(func):
    def wrapper(*args,**kwargs):
        wrapper.calls+=1
        print(f"call #{wrapper.calls} of '{ func.__name__}'")
        return func(*args,**kwargs)
    

    wrapper.calls =0
    return wrapper 


@function
def greet(name):
    print(f"heloo ,{name}")


greet("navya")
greet("neha")
greet("nandhu")

print("total calls",greet.calls)



