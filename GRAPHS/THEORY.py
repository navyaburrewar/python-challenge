# # GRAPHS

# # 1.collection of nodes or Data
# #  2.edges and  vertices (edge or vertices)

# # vertices /nodes   ex--> maps and sources

# # edges= connection b/w nodes or vertices 
# # link path from source to destination

# # G{V,E}




# #     (1)
# #    /   \
# #  (2)---(3)
# #   |     |
# #  (4)---(5)

# #  V = {1, 2, 3, 4, 5}
# #  E = {(1,2), (1,3), (2,3), (2,4), (3,5), (4,5)}



# # types of graphs
# # 1.directed graphs     ---> edges will have directions
# # 2.undirected graphs    --> no directions for the edges  we can go any side both sides
# # 3.weighted graphs     ---->edges will have weights  
# # 4 .unweighted graph    ---> no weights on the edges
# # 5.connected graphs      -->all the nodes are conneted by the edges
# # un-connected graph or disconnected    --> vertices in the grapfh may /may not br connected by edge
# # cyclic                  --->cyclic or closed graph
# # as.cycle graph           --> no cyclic path connection



# #  2 ways to represent the graths

# # 1.adjacent list
# # 2.adjacent matrix

# # 1.adjacent list

# g=[(1,2),(2,4),(4,9),(9,3),(3,1),(1,9)]

# adj={}

# for u,v in g:
#     if u not in adj:
#         adj[u]=[]
#     if v not in adj:
#         adj[v]=[]

#     adj[u].append(v)
#     adj[v].append(u)

# print(adj)            





# dic={}
# for i in g:
#     if i[0]  not in dic:
#         dic[i[0]]=[]
#     dic[i[0]].append(i[1])
#     if i[1] not in dic:
#         dic[i[1]]=[]
#     dic[i[1]].append(i[0])

# print(dic)             



# #  matrix form

# #     (1)
# #    /   \
# #  (2)---(3)
# #   |     |
# #  (4)---(5)


# # 1 2 3 4 5
# # 1 [ 0 1 1 0 0 ]
# # 2 [ 1 0 1 1 0 ]
# # 3 [ 1 1 0 0 1 ]
# # 4 [ 0 1 0 0 1 ]
# # 5 [ 0 0 1 1 0 ]



# '''
# Graph and matrix for weighted graph
# g=[(v,v,w)]
# Eg: g=[(0,1,3),(1,2,9),(2,3,5),(3,0,6),(0,2,11),(1,3,2)]
#         3
#    (0)------(1)
#     |\      /|
#     | \11  / |
#    6|  \  / 2|9
#     |   \/   |
#     |   /\   |
#    (3)------(2)
#         5

#     0  1  2  3
# 0 [ 0, 3,11, 6 ]
# 1 [ 3, 0, 9, 2 ]
# 2 [11, 9, 0, 5 ]
# 3 [ 6, 2, 5, 0 ]
       
# '''
# G=[(0,1,3),(1,2,9),(2,3,5),(3,0,6),(0,2,1),(1,3,2)]
# n=4

# matrix=[]
# for i in range(0,n):
#     r=[]
#     for j in range(0,n):
#         r.append(0)
#     matrix.append(r)
# for i in G:
#     matrix[i[0]][i[1]] =i[2]
#     matrix[i[1]][i[0]]=i[2]
# print(matrix)    





# adj={
#     0:[1,2,3],
#     1:[0,2,3],
#     2:[0,1,3],
#     3:[0,2,1]
# }
# n=4

# matrix=[]
# for i in range(n):
#     r=[]
#     for j in range():
#         r.append(0)
#     matrix.append(r)




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
            







