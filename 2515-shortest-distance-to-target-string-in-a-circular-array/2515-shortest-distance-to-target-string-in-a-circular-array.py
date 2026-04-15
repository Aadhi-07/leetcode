class Solution:
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        ans = n
        
        for i in range(n):
            if words[i] == target:
                d1 = (i - startIndex + n) % n
                d2 = (startIndex - i + n) % n
                ans = min(ans, d1, d2)
        
        return ans if ans != n else -1