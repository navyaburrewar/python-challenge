# Use lambda inside sorted() to sort words based on:
# Last character of each word


friuts =["apple","mango","banana"]

order = sorted(friuts ,key=lambda x:x[-1])
print(order)
