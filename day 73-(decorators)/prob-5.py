## 4 4️⃣ Replace Return Value

# Write a decorator that ignores the original return value and always returns:
# "Access Denied"


def function(func):
    def inner():
        return  "access deined"
    return inner

@function
def my_func():
    return "choti"
print(my_func())    




