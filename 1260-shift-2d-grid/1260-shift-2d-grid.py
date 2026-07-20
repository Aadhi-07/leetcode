class Solution(object):
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        flat = []

        for row in grid:
            flat.extend(row)

        total = m * n
        k %= total

        flat = flat[-k:] + flat[:-k]

        ans = []
        idx = 0

        for i in range(m):
            ans.append(flat[idx:idx + n])
            idx += n

        return ans