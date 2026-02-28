class Solution:
    def maximumXor(self, s, t):
        z = t.count('0')
        o = t.count('1')
        r = []
        
        for c in s:
            if c == '0':
                if o:
                    r.append('1')
                    o -= 1
                else:
                    r.append('0')
                    z -= 1
            else:
                if z:
                    r.append('1')
                    z -= 1
                else:
                    r.append('0')
                    o -= 1
        
        return ''.join(r)