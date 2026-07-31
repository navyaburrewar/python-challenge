## singly linked list

class Node:
    def __init__(self,num):
        self.data=num
        self.Next=None

class SLL:
    def __init__(self):
        self.head=None

    def add_end(self,num):
        new=Node(num)    
        if self.head is None:
            self.head=new
        else:
            tc=self.head
            while tc.Next is not  None : 
                tc=tc.Next
            tc.Next=new  
    def psll(self):
        if self.head is None:
            print("no data")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end="-->")  
                temp=temp.Next
            print("temp getout from the train")             
    def add_begin(self,num):
        new=Node(num)
        if self.head is None:
            self.head=new
        else:
            new.next=self.head
            self.head=new   
    def delete_end(self):
        if self.head==None:
            print("empty")
        elif self.head.Next==None:
            self.head=None
        else:
            temp=self.head
            while temp.Next.Next is not None:
                temp=temp.Next   
            temp.Next=None                         
    def insert(self,data,pos):
        new=Node(data)
        if self.head is None or pos==0:
            self.head=new
        else:
            c=0
            temp=self.head
            pos=pos-1
            while pos!=c and temp.Next!=None:
                temp=temp.Next
                c+=1
            new.Next=temp.Next
            temp.Next=new    



T=SLL()
T.add_begin(200)
T.add_end(10)
T.add_end(20)
T.add_end(30)
T.delete_end()
T.insert(80,5)
T.insert(90,2)
T.psll()




##Variable sliding window ---------
# nums = [2,3,1,2,4,3]


def longest_subarr(nums, k):

    left =0
    
    max_len = 0
    total=0

    for right in range(len(nums)):
        total += nums[right]
        #print(total)

        while total>k:
            total-=nums[left]

            left+=1
            #best subarray
            if right-left+1 > max_len:
                max_len = right-left+1

                st = left
                en = right

    return nums[st:en+1], max_len
                
    

arr = [2,3,1,2,4,3]
n=7
print(longest_subarr(arr,n))
