class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #intialze a hashmap
        count = {}
        #initialze the array we are using for bucket sort
        freq = [[] for i in range(len(nums) + 1)]
        #sort ttrough nums and populate hashmap
        for num in nums:
            count[num] = 1 + count.get(num,0)
        #now we need to populate our key value pairs of the map into the array
        for num,cnt in count.items():
            freq[cnt].append(num)
        res = []
        #iterate backwards
        for i in range(len(freq) - 1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            