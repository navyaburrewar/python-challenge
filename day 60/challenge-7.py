#3 Write a function that counts vowels in a string

def counting_vowels(name):
    count=0
    vowels = "aeiou"
    for char in name:
        if char in vowels:
           count+=1

    return count
     

print(counting_vowels("navya"))     
