
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        index_nums1 = 0
        index_nums2 = 0

        if n == 0:
            return
        
        if m == 0:
            nums1[:] = nums2[:]
            return
        
        for i in range(m + n):
            if index_nums2 == n:
                return
            
            if index_nums1 >= m + index_nums2:
                nums1[index_nums1] = nums2[index_nums2]
                index_nums1 += 1
                index_nums2 += 1
            
            
            elif (nums2[index_nums2] < nums1[index_nums1]):
                nums1.insert(index_nums1, nums2[index_nums2])
                nums1.pop(-1)
                index_nums1 += 1 # Only because we inserted though
                index_nums2 += 1
        
            else:
                index_nums1 += 1
            
        
    
            
            
if __name__ == "__main__":
    test = Solution()
    
    
    # Test case 1
    nums1 = [-10,-10,-9,-9,-9,-8,-8,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-3,-3,-2,-2,-1,-1,0,1,1,1,2,2,2,3,3,3,4,5,5,6,6,6,6,7,7,7,7,8,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    m = 55
    nums2 = [-10,-10,-9,-9,-9,-9,-8,-8,-8,-8,-8,-7,-7,-7,-7,-7,-7,-7,-7,-6,-6,-6,-6,-5,-5,-5,-5,-5,-4,-4,-4,-4,-4,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,9,9,9,9]
    n = 99

    testArray = sorted([-10,-10,-9,-9,-9,-8,-8,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-3,-3,-2,-2,-1,-1,0,1,1,1,2,2,2,3,3,3,4,5,5,6,6,6,6,7,7,7,7,8,9,9,9,9,-10,-10,-9,-9,-9,-9,-8,-8,-8,-8,-8,-7,-7,-7,-7,-7,-7,-7,-7,-6,-6,-6,-6,-5,-5,-5,-5,-5,-4,-4,-4,-4,-4,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,9,9,9,9])


    test.merge(nums1, m, nums2, n)
    print(nums1)

    # assert(nums1 == testArray)


    # Test case 2
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    test.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1,0]
    m = 1
    nums2 = [2]
    n = 1

    test.merge(nums1, m, nums2, n)
    print(nums1)
    
    
    nums1 = [-1,0,0,0,3,0,0,0,0,0,0]
    m = 5
    nums2 = [-1,-1,0,0,1,2]
    n = 6

    test.merge(nums1, m, nums2, n)
    print(nums1)
    
    
    nums1 = [4,0,0,0,0,0]
    m = 1
    nums2 = [1,2,3,5,6]
    n = 5

    test.merge(nums1, m, nums2, n)
    print(nums1)