## sliding window

# a="sadbustsad"
# b="sad" 
# l=len(b)
# c=0
# for i in range(0,len(a)-l+1):
#     if a[i:i+3 ]==b:
#         c+=1
# print(c)

# sum of windows
a=[1,2,3,4,5]
w=2

for i in range(0,len(a)-w+1):
    sum=0
    for k in a[i:i+w]:
        sum+=k
    print(sum,end=" ")    