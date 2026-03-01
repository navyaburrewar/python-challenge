# 1️⃣3️⃣

# Use lambda with map() to flatten this list:
# [[1, 2], [3, 4], [5, 6]]
# (Without using loops directly)

nums = [ [1, 2], [3, 4], [5, 6]]

flattenred =list(map(lambda x:x[0],nums  )) +list(map(lambda x:x[1],nums))
print(flattenred)