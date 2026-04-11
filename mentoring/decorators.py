def decorator(func):
    def inner():
      
        print(func()*2)
    return inner
    


@decorator

def my_func():
   
   return 3
    
my_func()

