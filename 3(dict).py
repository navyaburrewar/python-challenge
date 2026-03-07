# ## Given a string, find the first non-repeating character using a dictionary.


# ch=input("enter:  ")   

# count={}

# for char in ch:
#     if char in count:
#         count[char]+=1
#     else :
#         count[char]=1


# for key,value in count.items():
#     if value==1:
#         print(key)            





## Take a sentence from the user and count how many times each word appears.


sentence =input("enter a sentence:  ").split()

count={}

for word in sentence:
    if word in count:
        count[word]+=1
    else:
        count[word]=1


for key ,value in count.items():
    print(key,":",value)            





