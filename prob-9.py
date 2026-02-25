## Create a function that builds a dictionary from *args assuming arguments are given in key-value pairs.

def func(*marks):
    if len(marks)% 2 != 0:
     print("argument must in key -value formate")
     return
    

    result ={}
    for i in range(0,len(marks),2):
       key =marks[i]
       value = marks[i+1]
       result[key]=value

    print(result)

func("telugu",40 , "hindhi", 30 ,"sc",39 , "gk", 100)       