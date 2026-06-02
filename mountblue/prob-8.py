

def superReducedString(s):
    s=list(s)
    i=0
    while i<len(s)-1:
       if s[i]==s[i+1]:
           del s[i]
           del s[i]
           
           i=0
       else:
           i+=1
           

   
    result= "".join(s)    
    if result == "":
        return "Empty String"
    else:
        return result      

s="abbccs"
print(superReducedString(s))    

           