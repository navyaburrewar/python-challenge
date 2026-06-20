# 8. Sort Student Marks

# Sort student marks while keeping the corresponding names together.

# input
# names = ["Ravi", "Priya", "Arjun", "Neha"]
# marks = [75, 92, 68, 85]

# expected output
# names = ["Arjun", "Ravi", "Neha", "Priya"]
# marks = [68, 75, 85, 92]

def funct(arr,names):
    for i in range(1,len(arr)):
        
        key=arr[i]
        key_name=names[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            names[j+1]=names[j]
            j-=1
        arr[j+1]=key
        names[j+1]=key_name
    return arr, names
print(funct([75, 92, 68, 85]
,["Ravi", "Priya", "Arjun", "Neha"])  )       


