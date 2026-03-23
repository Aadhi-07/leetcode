class Solution:
    def maxProductPath(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        mx = [[0]*n for _ in range(m)]
        mn = [[0]*n for _ in range(m)]
        
        mx[0][0] = mn[0][0] = grid[0][0]
        
        for i in range(1, m):
            mx[i][0] = mn[i][0] = mx[i-1][0] * grid[i][0]
        
        for j in range(1, n):
            mx[0][j] = mn[0][j] = mx[0][j-1] * grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                x = grid[i][j]
                
                a = mx[i-1][j] * x
                b = mn[i-1][j] * x
                c = mx[i][j-1] * x
                d = mn[i][j-1] * x
                
                mx[i][j] = max(a, b, c, d)
                mn[i][j] = min(a, b, c, d)
        
        res = mx[m-1][n-1]
        
        if res < 0:
            return -1
        
        return res % (10**9 + 7)