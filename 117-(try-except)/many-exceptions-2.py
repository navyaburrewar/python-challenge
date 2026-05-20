# Many Exceptions

# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

try:
  print(x)
except NameError:
  print("variable x is not defined")
except:
  print("something else went wrong")  


## hence in the about the in exception it was given that name error
#  hence it will print("variable x is not defined")


try:
  print(x)
except ValueError:
  print("variable x is not defined")
except:
  print("something else went wrong")  

#  for the about code it will tell as that some thing went wrong beause that
#  excpetion value error is not correct hence it will give the 
#  hence it will give sent print statement