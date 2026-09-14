class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #iterate through the array
        #keep track of each numbers occurance
        counts = {}
        #if at any point during the iteration a numbers occurance reaches 2, return true
        #if not then return false
        for n in nums:
            #store each occurance in something
            counts[n] = counts.get(n,0) + 1
            if counts[n] > 1:
                return True
        return False


            


