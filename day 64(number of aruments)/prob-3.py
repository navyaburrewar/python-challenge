#3 Raise a custom error if fewer than 2 arguments are passed.

def funct(*args):
    if len(args)<2 :
        print("custom error")
    else:    
       print("valid argument:",args)

funct(29)        