class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #get the frequence of each string using an array of size 26, and store that into an array and use that as a key for the map
        #everytime we run into an array with this specific key we add it to its value
        hashmap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in hashmap:
                hashmap[key] = [s]
            else:
                hashmap[key].append(s)
    
        return list(hashmap.values())