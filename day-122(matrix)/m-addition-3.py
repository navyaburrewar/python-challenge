
### ======== understanding of the loopin in matrix==========#

# ✔️ What you said (corrected version)

# You said:

# first it will select the row for first for loop and second loop will go over that row like [0,0],[0,1]...

# ✔️ YES — that is correct.

# Just refine this part:

# “then it will come out of second loop then again it will move to first row”

# ✔️ More accurate version:

# It does NOT “come out and move”
# Instead:
# 👉 Inner loop finishes completely
# 👉 Then outer loop automatically moves to next i



##==========addition ============##

m1=[[1,2,3],
    [2,3,4],
    [3,4,5]]

m2=[[3,4,5],
    [4,5,6],
    [5,6,7]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

row=3
col=3
for i in range(row):
    for j in range(col):
        result[i][j]=m1[i][j]+m2[i][j]
print(result)        