class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seenAlready = False
        k = 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] == nums[i] and not seenAlready:
                seenAlready = True
                k += 1
            elif nums[i-1] < nums[i]:
                seenAlready = False
                k += 1
            else:
                nums.append(nums[i-1])
                nums.pop(i-1)
        
        return k
        

                
            
        

if __name__ == "__main__":
    test = Solution()
    nums = [1,1,1,2,2,3]
    
    print(test.removeDuplicates(nums))
    print(nums)
    
    nums = [0,0,1,1,1,1,2,3,3]
    
    print(test.removeDuplicates(nums))
    print(nums)

