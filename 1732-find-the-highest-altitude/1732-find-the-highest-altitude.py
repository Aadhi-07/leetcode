class Solution(object):
    def largestAltitude(self, gain):
        cur = 0
        ans = 0
        
        for x in gain:
            cur += x
            if cur > ans:
                ans = cur
        
        return ans