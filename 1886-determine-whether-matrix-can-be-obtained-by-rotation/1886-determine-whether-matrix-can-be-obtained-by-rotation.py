class Solution:
    def findRotation(self, mat, target):
        n = len(mat)
        
        def rot(m):
            return [[m[n-1-j][i] for j in range(n)] for i in range(n)]
        
        for _ in range(4):
            if mat == target:
                return True
            mat = rot(mat)
        
        return False