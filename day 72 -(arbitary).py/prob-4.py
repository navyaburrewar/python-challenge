
# Create a function that multiplies all numbers passed using *args.

def function(*args):
    result =1
    for i in args:
      result*=i
    return result

print(function(20,39,10) )   