class Solution:
    def numberOfStableArrays(self, zero, one, limit):
        mod = 1000000007
        
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]
        
        for z in range(1, min(limit, zero)+1):
            dp0[z][0] = 1
        for o in range(1, min(limit, one)+1):
            dp1[0][o] = 1
        
        for z in range(zero+1):
            for o in range(one+1):
                if z > 0 and o > 0:
                    dp0[z][o] = (dp1[z-1][o] + dp0[z-1][o]) % mod
                    if z-limit-1 >= 0:
                        dp0[z][o] = (dp0[z][o] - dp1[z-limit-1][o]) % mod
                    
                    dp1[z][o] = (dp0[z][o-1] + dp1[z][o-1]) % mod
                    if o-limit-1 >= 0:
                        dp1[z][o] = (dp1[z][o] - dp0[z][o-limit-1]) % mod
        
        return (dp0[zero][one] + dp1[zero][one]) % mod