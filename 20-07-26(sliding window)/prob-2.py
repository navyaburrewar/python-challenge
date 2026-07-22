## prime number
n=int(input())
output=[]
for j in range(1,int(n**(0.5))):
    count=0
    for i in range(1,n+1):
       if j%i==0:
            count+=1
    if count==2:
        output.append(j)
print(output)        
        
   

