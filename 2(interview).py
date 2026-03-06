#   ## lst = user input, print non repeating numbers from the given list [10, 20,16, 23, 12, 25, 16, 16, 10, 20]--23,12,25  




# user input
lst = list(map(int, input("Enter numbers separated by space: ").split()))

count = {}

# count frequency
for num in lst:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

# print non-repeating numbers
for key, value in count.items():
    if value == 1:
        print(key)