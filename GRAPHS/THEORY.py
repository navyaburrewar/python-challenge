# GRAPHS

# 1.collection of nodes or Data
#  2.edges and  vertices (edge or vertices)

# vertices /nodes   ex--> maps and sources

# edges= connection b/w nodes or vertices 
# link path from source to destination

# G{V,E}




#     (1)
#    /   \
#  (2)---(3)
#   |     |
#  (4)---(5)

#  V = {1, 2, 3, 4, 5}
#  E = {(1,2), (1,3), (2,3), (2,4), (3,5), (4,5)}



# types of graphs
# 1.directed graphs     ---> edges will have directions
# 2.undirected graphs    --> no directions for the edges  we can go any side both sides
# 3.weighted graphs     ---->edges will have weights  
# 4 .unweighted graph    ---> no weights on the edges
# 5.connected graphs      -->all the nodes are conneted by the edges
# un-connected graph or disconnected    --> vertices in the grapfh may /may not br connected by edge
# cyclic                  --->cyclic or closed graph
# as.cycle graph           --> no cyclic path connection



#  2 ways to represent the graths

# 1.adjacent list
# 2.adjacent matrix

# 1.adjacent list

g=[(1,2),(2,3),(3,4),(4,1),(2,4),(1,3)]
