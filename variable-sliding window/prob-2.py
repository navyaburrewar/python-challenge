# Problem 2: Longest Substring with At Most K Distinct Characters


def logest_sub(nums,k):
    left=0
    word=""
    max_len=0
    for  right in range(len(nums)):
        word+=(nums[right])

        while len(set(word))>k:
            word=word[1:]
            left+=1

        max_len=max(max_len,right-left+1)


    return max_len
s="eceba"
print(logest_sub(s,2))        

