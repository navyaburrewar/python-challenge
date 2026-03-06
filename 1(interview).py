

# lst= 0,16, 23, 12, 25, 16, 16, 10, 20]-- print the number which comes k=3 times using dictioneries


lst = [0, 16, 23, 12, 25, 16, 16, 10, 20]

count = {}

for num in lst:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

# Print number which comes 3 times
for key, value in count.items():
    if value == 3:
        print( key)



       