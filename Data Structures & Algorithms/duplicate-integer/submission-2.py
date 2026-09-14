class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #loop through array and omapre it to whats in the set
        #if its not in set, continue looping
        #if in set, return true

        duplicates = set()
        
        for n in nums:
            if n in duplicates:
                return True
            else:
                duplicates.add(n)
        return False