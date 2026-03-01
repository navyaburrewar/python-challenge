## Use lambda with filter() to extract only odd numbers from a list.
num =[32,43,54,20,9,47]

odd_num = list(filter(lambda x : x%2!=0, num))
print(odd_num)