# ===========  1 way ============ #
"""
m1=[[1,2,3],
    [2,3,4]]

taget=5

for i in range(2):
    for j in range(3):
        if m1[i][j]==taget:
            print("found")
            exit()
else :
    print("not")
"""

# ============== 2nd  way ==============#
"""
m1=[[1,2,3],
    [2,3,4]]

taget=1

for i in range(2):
    for j in range(3):
        if m1[i][j]==taget:
            print("found")
            break
    else:
        continue

    break
    
else :
    print("not")
"""