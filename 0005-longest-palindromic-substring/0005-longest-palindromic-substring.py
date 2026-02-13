class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        st = 0
        mx = 1
        
        def exp(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        for i in range(n):
            a = exp(i, i)       
            b = exp(i, i + 1)   
            cur = max(a, b)
            
            if cur > mx:
                mx = cur
                st = i - (cur - 1) // 2
        
        return s[st:st + mx]
