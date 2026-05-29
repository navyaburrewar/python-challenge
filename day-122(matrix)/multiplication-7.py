a=[[1,2,3],
   [2,3,4],
   [3,4,5]]

b=[[1,2],
   [2,3],
   [3,4]]

result=[]
for i in range(len(a)):          # here len(a) is an row                                   
    row=[0]*len(b[0])            # here len(b[0])  is no of colums --> instill get confude refer matrix-1.py
    for j in range(len(b[0])):      
        for k in range(len(b)):
            row[j]+=a[i][k]*b[k][j]
    result.append(row)
print(result)            

