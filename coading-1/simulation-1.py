class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        word_1=""
        
       
        for move in moves:
            if move!="_" :
                word_1+=move
            else:    
                word_1+="L"  

        word_2=""          
        for move in moves:
            if move!="_" :
                word_2+=move
            else:    
                word_2+="R"  
 
        count_1=0
        for i in word_1:
            if i=="L":
                count_1+=1
            else:
                count_1-=1    
        count_2=0
        for j in word_2:
            if j=="R":
                count_2+=1
            else:
                count_2-=1

        return max(abs(count_1),abs(count_2)   )                 
        

        
            







        
    

                
       