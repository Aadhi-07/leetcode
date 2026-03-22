class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
        
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        x = 0
        while i < n and '0' <= s[i] <= '9':
            x = x * 10 + (ord(s[i]) - ord('0'))
            
            if sign * x <= -2147483648:
                return -2147483648
            if sign * x >= 2147483647:
                return 2147483647
            
            i += 1
        
        return sign * x