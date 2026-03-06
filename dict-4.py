lst = [1,2,3,4,5,6,6,62,1,0]

count = {}

for num in lst:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

max_count = 0
max_element = None

for key, value in count.items():
    if value > max_count:
        max_count = value
        max_element = key

print("Most frequent element:", max_element)
print("Count:", max_count)