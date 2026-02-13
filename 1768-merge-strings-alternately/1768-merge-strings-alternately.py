class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        i = 0
        j = 0
        res = ""
        
        while i < len(w1) and j < len(w2):
            res += w1[i]
            res += w2[j]
            i += 1
            j += 1
        
        res += w1[i:]
        res += w2[j:]
        
        return res
