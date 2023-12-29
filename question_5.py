class Solution:
    # For some reason, checking the length of the array and stopping if you hit that point
    # actually made it slower. Probably depends on the lists you are using.
    def majorityElement(self, nums: list[int]) -> int:
        current_num = 0
        current_times = 0
        # length_of_array = len(nums)
        # halfway = length_of_array // 2
        for i in range(len(nums)):
            if nums[i] != current_num:
                current_times -= 1
                
                if current_times < 0:
                    current_times = 1
                    current_num = nums[i]
            else:
                current_times += 1
            
            # if i > halfway and current_times > halfway:
            #     return current_num
        
        return current_num
        

                
            
        

if __name__ == "__main__":
    test = Solution()
    nums = [3,2,3]
    
    print(test.majorityElement(nums))
    
    nums = [2,2,1,1,1,2,2]
    
    print(test.majorityElement(nums))

