##Create a function using *args that finds the largest number among the arguments.

def func(*m):
    if len(m)==0:
        return 0
    max_num=m[0]
    for i in m:
        if i>max_num:
            i==max_num
    return max_num   

print(func(23,12,45,67,13) )
