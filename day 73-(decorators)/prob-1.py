# 1️⃣ Print Before & After

# Create a decorator simple_logger that prints:
# "Starting function..." before execution
# "Function finished." after execution
# Apply it to a function display().



def display(func):
    def inner():
        print("before execuation")
        result= func()
        print("after execuation")
        return result
    return inner
     

@display
def simple_logger():
    print("inside the function")
simple_logger()

    

