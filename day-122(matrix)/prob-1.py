def sockMerchant(n, ar):
    result=0
    i=0
    while i<len(ar):
      j=i+1
      while j<len(ar):
        if ar[i]==ar[j]:
          result+=1
            
          del ar[i]
          del ar[j-1]
            
          break  
        
        j+=1
      else:
        i+=1
                
                
                
                
    return result
n=7
ar=[3,7,1,7,4,3,4]
print(sockMerchant(len(ar),ar))