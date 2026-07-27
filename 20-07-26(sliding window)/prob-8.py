# [a, i, o, r, t, u, o]
# SUB Array having more number of vowels


arr=["a", "i","o", "r", "t","u","o","l"]
k=4
vowels=["a","e","i","o","u"]
count=0
for i in range(k):
    if arr[i] in vowels:
        count+=1
      
max_vowels=count
max_window=arr[:k]

for i in range(k,len(arr)):
    if arr[i] in vowels:
        count+=1
    if arr[i-k] in vowels:
        count-=1

    if count >max_vowels:
        max_vowels=count
        max_window=arr[i-k+1:i+1]

print(max_window)
print(max_vowels)        




