
# 6️⃣ Decorator with Arguments Support

# Write a decorator that works with functions that take arguments.

# Example:
# add(2, 3) → 5
# Decorator should print:
# Adding numbers...


def functin(func):
    def inner(a,b):
        print("adding numbers")
        result= func(a,b)
        return result
    return inner


@functin
def add(a,b):
    return a+b
print(add(8,3))