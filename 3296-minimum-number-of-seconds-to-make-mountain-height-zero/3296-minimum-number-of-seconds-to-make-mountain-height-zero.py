class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        def can(t):
            h = 0
            for w in workerTimes:
                x = int(( (1 + 8*t//w) ** 0.5 - 1 ) // 2)
                h += x
                if h >= mountainHeight:
                    return True
            return False
        
        l, r = 0, 10**18
        
        while l < r:
            m = (l + r) // 2
            if can(m):
                r = m
            else:
                l = m + 1
        
        return l