##2️⃣ Write a Logging Decorator

# Question:

# Create a decorator that logs:
# Function name
# Arguments passed
# Return value
# Example output:
# Calling add(2, 3)
# add returned 5


def function(func):
    def inner(a,b):
        return func(a,b)
    return inner

@function
def my_func(a,b):
    return a+b
print(my_func(23,60))