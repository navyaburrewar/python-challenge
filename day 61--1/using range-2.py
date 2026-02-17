
## using range

for i in range(10):
    print(i)



## using list to display the rages
# 
print(list(range(4)))    
print(list(range(4,8))) 
print(list(range(4,5,10))) 



##slicing ranges

r =range(10)
print(r[2:7])
print(r[: 5])

## membership testing

r=range(0,5,2)
print(4 in r)
print(5 in r)


##3 length
r=range(0,10,2)
print(len(r))