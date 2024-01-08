import re

class Solution:
    # For some reason, checking the length of the array and stopping if you hit that point
    # actually made it slower. Probably depends on the lists you are using.
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        canConstruct = True
        
        for i in ransomNote:
            if i in magazine:
                position = magazine.find(i)
                if position != -1:
                    magazine = magazine.replace(i, "", 1)
                else:
                    canConstruct = False
            else:
                canConstruct = False
        
       
       
       
        return canConstruct
        
        
        
    
    
           
        

                
            
        

if __name__ == "__main__":
    test = Solution()
    
    ransomNote = "a"
    magazine = "b"
    print(test.canConstruct(ransomNote, magazine))
    
    ransomNote = "aa" 
    magazine = "ab"
    print(test.canConstruct(ransomNote, magazine))
    
    ransomNote = "aa" 
    magazine = "aab"
    print(test.canConstruct(ransomNote, magazine))


