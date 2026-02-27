class Solution(object):
    def convert(self, s, n):
       
        if n == 1 or n >= len(s):
            return s

        r = [""] * n
        i = 0
        d = 0

        for c in s:
            r[i] += c
            if i == 0:
                d = 1
            elif i == n - 1:
                d = -1
            i += d

        return "".join(r)