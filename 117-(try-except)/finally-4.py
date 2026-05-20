#   finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the try excpet is finished")        



#  ex-2
try:
    print("20")
except:
    print("something went wrong")
else:
    print("every thing is fine")
finally:
    print("try-except is finished")
                