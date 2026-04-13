class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        w = len(words[0])
        n = len(words)
        m = len(s)
        
        need = {}
        for x in words:
            need[x] = need.get(x, 0) + 1
        
        res = []
        
        for i in range(w):
            l = i
            cur = {}
            cnt = 0
            
            for r in range(i, m - w + 1, w):
                word = s[r:r+w]
                
                if word in need:
                    cur[word] = cur.get(word, 0) + 1
                    cnt += 1
                    
                    while cur[word] > need[word]:
                        left = s[l:l+w]
                        cur[left] -= 1
                        l += w
                        cnt -= 1
                    
                    if cnt == n:
                        res.append(l)
                else:
                    cur.clear()
                    cnt = 0
                    l = r + w
        
        return res