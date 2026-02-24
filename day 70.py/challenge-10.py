# ## linear search
# from array import array

# arr=array('i',[2,4,6,8,9,12,34])

# k=4
# for i in range(len(arr)):
#     if arr[i]==k:
#         print(k)
#         break


# ###  A function that calculates the sum of any number of values:
# def func(*nums):
#     total=0
#     for num in nums:
#       total+=num
#     return total
# print(func(23,4,9,2,2))    



# def func(*alphabet):
#     total=""
#     for char in alphabet:
#       total+=char
#     return total  
# print(func("n","a","v","y","a"))


### unpackin with dictionaries with**
#If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

def func(fname,lname):
    print( "hello",fname,lname)

greeting = {"fname":"navya","lname":"burrewar"}
func(**greeting)

#ex-2
z=100
def func():
    x=200
    print(x)
func()
print(z)    



# def function(func):
    
#     return func().upper()


# @function
# def my_function():
#     return "hello world"

# print(my_function)



# def function(func):
#     def inner():
#         return func().lower()
#     return inner

# def my_function():
#     return "HELLO WORLD"


# print(my_function())


def marks(func):
    def sub(name):
        result=func(name)
        return result.upper()    
    return sub



@marks
def school(name):
    return("20 marks "+name)
print(school("akhi"))



def func(m):
    return lambda a:a+m
myfunc=func(6)
print(myfunc(4))



for i in range(1,4):
    for j in range(1,4):
        print(f"i={i}, j={j}")

#What this line does