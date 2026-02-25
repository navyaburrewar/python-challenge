##  Write a function that accepts a mix of normal parameters, *args, and **kwargs, and prints them in order.

def function(name ,*names ,**numbers):
    print("normal parameter", name)
    print("*names (args)",names )
    print("**number (kwargs)", numbers )

(function("navya","choti", marks=20,age=21))