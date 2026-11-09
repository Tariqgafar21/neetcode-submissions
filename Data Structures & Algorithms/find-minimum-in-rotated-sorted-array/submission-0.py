class Solution:
    def findMin(self, nums: List[int]) -> int:
        #how do we know how many times its sorted
        #do binary search on both parts of array
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        return nums[l]
            
    
            

       
        