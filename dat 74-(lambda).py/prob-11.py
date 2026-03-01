## Use lambda with sorted() to sort a list of strings alphabetically (case-insensitive).

names =["navya","nandhu","choti","neha"]

order = sorted (names ,key = lambda x :x [0] )
print(order)