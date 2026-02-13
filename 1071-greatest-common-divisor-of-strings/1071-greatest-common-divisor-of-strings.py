class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        if s1 + s2 != s2 + s1:
            return ""
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n = gcd(len(s1), len(s2))
        return s1[:n]
