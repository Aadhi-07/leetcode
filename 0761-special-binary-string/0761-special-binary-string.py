class Solution:
    def makeLargestSpecial(self, s):
        if not s:
            return s
        
        count = 0
        start = 0
        subs = []
        
        for i, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            
            if count == 0:
                inner = self.makeLargestSpecial(s[start+1:i])
                subs.append("1" + inner + "0")
                start = i + 1
        
        subs.sort(reverse=True)
        return "".join(subs)