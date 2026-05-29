mat=[]
rows=3
col=2


for i in  range(rows):
    row=[]
    for j in range(col):
        value=int(input("enter value: "))
        row.append(j)
    mat.append(row)
print(mat)        