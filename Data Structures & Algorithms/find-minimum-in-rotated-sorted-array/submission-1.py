class Solution:
    def findMin(self, nums: List[int]) -> int:
        #two pointers
        #check if the mid is less than or greater tha the right'
        #if greater move left to the mid
        #if less move right to mid -1
        l = 0
        r = len(nums) -1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                return nums[r]
            