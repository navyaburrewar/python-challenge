#### execute functions in F-Strings
# 

#  You can execute functions inside the placeholder:

### using string method upper()

fruit="apple"
text=f"i eat {fruit.upper()} regularlly"
print(text)


############## ex-2 ##############3
text=f"i eat {"mango".upper()} regularlly"
print(text)



################ ex-3 ######################
def myconverter(x):
    return x*5
text =f"the plane is flying at a {myconverter(20)}"
print(text)
