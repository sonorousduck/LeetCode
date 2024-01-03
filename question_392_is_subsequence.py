import re

class Solution:
    # For some reason, checking the length of the array and stopping if you hit that point
    # actually made it slower. Probably depends on the lists you are using.
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        
        s_index = 0
        
        for letter in t:
            if s[s_index] == letter:
                s_index += 1
                
                if s_index == len(s):
                    return True
       
       
        return False
        
        
        
    
    
           
        

                
            
        

if __name__ == "__main__":
    test = Solution()
    
    s = "abc"
    t = "ahbgdc"
    print(test.isSubsequence(s, t))
    
    s = "axc"
    t = "ahbgdc"
    print(test.isSubsequence(s, t))


