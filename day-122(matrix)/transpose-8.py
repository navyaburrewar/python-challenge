a=[[1,2,3],
   [2,3,4],
   [3,4,1],
   [1,3,4]]

transpose=[]
for j in range(len(a[0])):  #0,1,2
   row=[]
   for i in range(len(a)): #0,1,2,3
      row.append(a[i][j])
   transpose.append(row)
print(transpose)   

