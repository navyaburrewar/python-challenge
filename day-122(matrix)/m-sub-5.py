## ======= matric substraction =============###

m1=[[2,3,4],
    [3,4,5]]
m2=[[2,3,4],
    [3,4,5]]

re=[[0,0,0],
    [0,0,0]]
rows=2
col=3

for i in range(rows):
    for j in range(col):
        re[i][j]=m1[i][j]-m2[i][j]

print(re)        