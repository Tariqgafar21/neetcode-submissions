class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #loop through arrays strings
        #get frequencies using an  array to get the frequencies
        #add each array into a hashmap
        #map the count arrays to its list of like strings
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26# a...z
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())