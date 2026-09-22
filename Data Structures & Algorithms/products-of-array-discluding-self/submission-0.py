class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        r = [1] * len(nums)
        res = []

    #go r to l
        prefix = 1
        for n in range(len(nums)):
            l[n] = prefix
            prefix *= nums[n]
        postfix = 1
        for n in range(len(nums) -1, -1, -1):
            r[n] = postfix
            postfix *= nums[n]
    #loop through 2 arrays at in
        for i in range(len(l)):
            res.append(l[i] * r[i])
        return res
