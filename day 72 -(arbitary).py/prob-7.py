## Create a function decorator that uses *args and **kwargs to wrap another function

def funct(adding) :
    def inner(*neha,**akhi):
      result = adding(*neha,**akhi)
      return result
    return inner



@funct
def my_func(*numm ,**names):
    print("numm" , numm  )
    print("names", names)
my_func("20", navya = "choti")
