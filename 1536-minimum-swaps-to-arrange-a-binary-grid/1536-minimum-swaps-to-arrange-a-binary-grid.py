class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        z = []
        
        for r in grid:
            c = 0
            for x in r[::-1]:
                if x == 0:
                    c += 1
                else:
                    break
            z.append(c)
        
        ans = 0
        
        for i in range(n):
            need = n - 1 - i
            j = i
            while j < n and z[j] < need:
                j += 1
            
            if j == n:
                return -1
            
            while j > i:
                z[j], z[j-1] = z[j-1], z[j]
                ans += 1
                j -= 1
        
        return ans