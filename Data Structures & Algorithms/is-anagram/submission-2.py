class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1 = {}
        s2 = {}

        for char in s:
            s1[char] = s1.get(char, 0) + 1
        
        for char in t:
            s2[char] = s2.get(char, 0) + 1

        for key in s1:
            if key not in s2 or s1[key] != s2[key]:
                return False
    
        return True
