class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        
        while x != 0:
            d = int(x % 10)
            if x < 0 and d > 0:
                d -= 10
            
            x = (x - d) // 10
            if res > 214748364 or res < -214748364:
                return 0
            
            res = res * 10 + d
        
        return res
