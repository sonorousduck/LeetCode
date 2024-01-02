import re

class Solution:
    # For some reason, checking the length of the array and stopping if you hit that point
    # actually made it slower. Probably depends on the lists you are using.
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Remove all non-alphanumeric characters and convert to lowercase
        s = re.sub("[^0-9a-zA-Z]", "",  s.lower())
        
        
        front_index = 0
        back_index = len(s) - 1
        
        while front_index < back_index:
            if s[front_index] != s[back_index]:
                return False
            
            front_index += 1
            back_index -= 1
        
        return True
        
        
        
    
    
           
        

                
            
        

if __name__ == "__main__":
    test = Solution()
    
    s = "A man, a plan, a canal: Panama"
    print(test.isPalindrome(s))
    
    s = "race a car"
    print(test.isPalindrome(s))
    
    s = " "
    print(test.isPalindrome(s))
    

