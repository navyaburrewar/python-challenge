# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example


# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

# Function Description

# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):

# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns

# int: the number of pairs
# Input Format

# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers, , the colors of the socks in the pile.

# Constraints

#  where 
# Sample Input

# STDIN                       Function
# -----                       --------
# 9                           n = 9
# 10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# Sample Output

# 3
# Explanation

# sock.png


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