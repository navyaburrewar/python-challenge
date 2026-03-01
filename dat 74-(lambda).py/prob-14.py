##Use lambda with filter() to get all numbers divisible by both 3 and 5 from a list.

nums =[3,15,45,8,9]
value = list(filter(lambda x :x%3 ==0 and x%5==0,nums ))
print(value)