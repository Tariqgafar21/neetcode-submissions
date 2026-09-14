class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #loop through the array starting at index 0
        #delcare var for the num to find
        #loop through until you find that num
        #return two indicies
        seenMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seenMap:
                return [seenMap[diff], i]
            seenMap[n] = i
        return