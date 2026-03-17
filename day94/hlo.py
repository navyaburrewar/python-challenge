## command line arguments

## mainthig is below line
# When you run a Python script from the terminal, you can pass extra values.

# ▶ sys.argv
# A list that stores command-line arguments.
# sys.argv[0] → script name
# sys.argv[1] → first argument
# sys.argv[2] → second argument …



## use this think to make it more flexsible 
## faster
## easy automatic


## if e want more values we dont want to edit the  complete or we dont open the file simple we give in the input 
## and it was always first prints the file name
## that is sys.argv[0] is always an file name


## prob-1


import sys
if len(sys.argv)>1:
  name = sys.argv[2]
  print("hello",name)
else:
  print("please provide your name as arguments")
    







