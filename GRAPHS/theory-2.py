dic={
    0:[2,4],
    1:[3,2],
    2:[0,1],
    3:[2,1,0],
    4:[2]
}
root =2
n=len(dic)
visited=[]
for i in range(n):
    visited.append(0)
a=[root]
op=[]
while len(a)!=0:
    k=a.pop()
    op.append(k)
    visited[k]=1

    for j in dic[k]:
        if visited[j]==0:
            visited[j]=1
            a.append(j)
print(op)
            







