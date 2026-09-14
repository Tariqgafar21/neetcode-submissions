class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            #loop through both the strings and put into map
            count1 = {} 
            count2 = {}
        for char in s:
            #populate
            count1[char] = count1.get(char, 0) + 1
        
        for c in t:
            count2[c] = count2.get(c, 0) + 1
        

        #check frequencies of each character in both maps are equal
                
        for key in count1:
            if count1[key] != count2.get(key, 0):
                return False
        return True