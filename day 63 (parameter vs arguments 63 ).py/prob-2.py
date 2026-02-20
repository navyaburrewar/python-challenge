## Create a function and call it with fewer arguments — handle the error using defaults.


def func(a,b,c=39):
    return (a,b,c)
print(func(30,29))