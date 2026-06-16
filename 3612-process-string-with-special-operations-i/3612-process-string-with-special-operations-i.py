class Solution:
    def processStr(self, s):
        r = []

        for c in s:
            if 'a' <= c <= 'z':
                r.append(c)
            elif c == '*':
                if r:
                    r.pop()
            elif c == '#':
                r.extend(r)
            else:  # '%'
                r.reverse()

        return ''.join(r)