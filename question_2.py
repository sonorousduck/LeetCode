class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums.sort()
        
        start_index = -1
        end_index = -1
        for i in range(len(nums)):
            if nums[i] == val and start_index == -1:
                start_index = i
            
            if start_index != -1 and nums[i] != val and end_index == -1:
                end_index = i
        
        if start_index != -1 and end_index == -1:
            end_index = len(nums)
        
        for _ in range(end_index - start_index):
            nums.pop(start_index)
        
        return len(nums)
                
            
        

if __name__ == "__main__":
    test = Solution()
    
    
    nums = [4, 5]
    val = 4
    
    print(test.removeElement(nums, val))
    print(nums)
        
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    
    print(test.removeElement(nums, val))
    print(nums)
    