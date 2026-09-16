class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_pairs = {}
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff  in index_pairs:
                 return [index_pairs[diff], n]
            else:
                index_pairs[nums[n]] = n
        return []