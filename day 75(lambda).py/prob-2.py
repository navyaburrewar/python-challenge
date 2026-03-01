# First → second value (ascending)
# If second values are equal → sort by first value (descending)

data = [(1, 3), (2, 2), (4, 2), (3, 1)]

sort =sorted(data,key=lambda x: (x[1], -x[0]))
print(sort)



## -x[1] here which will indiactes the decending order
