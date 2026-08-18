class Solution(object):
    def findRotation(self, mat, target):
        
        for _ in range(4):
            if mat == target:
                return True

            n = len(mat)

            # Rotate 90 degrees clockwise
            mat = [list(row) for row in zip(*mat[::-1])]

        return False