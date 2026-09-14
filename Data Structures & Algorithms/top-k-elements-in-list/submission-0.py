class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #map to store frequencies of nums in array
        freq = {}

        #loop through array
        for n in nums:
             freq[n] = freq.get(n, 0) + 1
        
        #loop through values
        result = []

        for key, value in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]:
            result.append(key)
   
        return result
