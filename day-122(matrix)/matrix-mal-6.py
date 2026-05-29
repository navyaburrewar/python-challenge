a=[[1,2],
    [3,4]]

b=[[4,5],[1,2]]


re=[[0,0],[0,0]]
for i  in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            re[i][j]+=a[i][k]*b[k][j]

print(re)            