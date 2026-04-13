#   problem-1
#   # print the one by one values as per the user input --
# input: 100
# output: line by line values which are divisible by 3


def div(m):
    for i in range(m) :
        if i%5==0:
            yield i
        
m=int(input())
for j in div(m):
    print(j)
