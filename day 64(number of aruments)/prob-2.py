# Modify it to accept variable number using *args.

def number(*args):
    return args

print(number(1,2,3,4,5))
print(number(2,3,6,4))