from collections import defaultdict

class Solution(object):
    def minScore(self, n, roads):
        graph = defaultdict(list)

        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        visited = set()
        ans = [float('inf')]

        def dfs(node):
            visited.add(node)

            for nei, dist in graph[node]:
                ans[0] = min(ans[0], dist)

                if nei not in visited:
                    dfs(nei)

        dfs(1)
        return ans[0]