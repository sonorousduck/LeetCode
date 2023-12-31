class Solution:
    # For some reason, checking the length of the array and stopping if you hit that point
    # actually made it slower. Probably depends on the lists you are using.
    def rotate(self, nums: list[int], k: int) -> None:
        # One way!
        # new_positions = {}
        
        # for i in range(len(nums)):
        #     new_positions[(i + k) % len(nums)] = nums[i]
        
        # for i in range(len(nums)):
        #     nums[i] = new_positions[i]
            
        # Another way
        steps = k % len(nums)
        nums[:] = nums[-steps:] + nums[:-steps]
        
        
        
    
    
           
        

                
            
        

if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    test.rotate(nums, k)
    print(nums)
    
    nums = [-1,-100,3,99]
    k = 2
    test.rotate(nums, k)
    print(nums)

