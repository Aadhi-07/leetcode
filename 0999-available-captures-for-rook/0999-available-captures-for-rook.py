class Solution:
    def numRookCaptures(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r, c = i, j
        
        ans = 0
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for x, y in d:
            i, j = r, c
            while 0 <= i < 8 and 0 <= j < 8:
                i += x
                j += y
                
                if not (0 <= i < 8 and 0 <= j < 8):
                    break
                
                if board[i][j] == 'B':
                    break
                if board[i][j] == 'p':
                    ans += 1
                    break
        
        return ans