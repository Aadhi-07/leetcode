class Solution:
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        c = 0
        while i >= 0 and s[i] != ' ':
            c += 1
            i -= 1
        
        return c