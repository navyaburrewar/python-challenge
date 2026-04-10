def decorator(func):
    def inner():
      
        print(func()*2)
    return inner
    


@decorator

def func():
   
   return int(input())  
    
func()

