class Solution:
    def champagneTower(self, p: int, r: int, g: int) -> float:
        dp = [[0.0] * 100 for _ in range(100)]
        dp[0][0] = p
        
        for i in range(r):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    extra = (dp[i][j] - 1) / 2
                    dp[i][j] = 1
                    dp[i+1][j] += extra
                    dp[i+1][j+1] += extra
        
        return min(1, dp[r][g])
