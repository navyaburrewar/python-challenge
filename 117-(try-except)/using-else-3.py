# using else:

# You can use the else keyword to define a block of code to be executed if no errors were raised:

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")  #---> print this line
 



# ex-2

try:
    print(90)
except:
    print("something went wrong")
else:    
    print("nothing went wrong")    # prints this line
      

# ex-3
try:
    print(nav)
except:
    print("something went wrong")
else:
    print("all fine")              