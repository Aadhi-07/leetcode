from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        m = len(grid)
        n = len(grid[0])

        health -= grid[0][0]
        if health <= 0:
            return False

        q = deque([(0, 0, health)])
        best = [[-1] * n for _ in range(m)]
        best[0][0] = health

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, h = q.popleft()

            if (r, c) == (m - 1, n - 1):
                return True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    nh = h - grid[nr][nc]

                    if nh > 0 and nh > best[nr][nc]:
                        best[nr][nc] = nh
                        q.append((nr, nc, nh))

        return False