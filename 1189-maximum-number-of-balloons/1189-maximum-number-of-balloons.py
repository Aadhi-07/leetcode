class Solution(object):
    def maxNumberOfBalloons(self, text):
        d = {}

        for c in text:
            d[c] = d.get(c, 0) + 1

        return min(
            d.get('b', 0),
            d.get('a', 0),
            d.get('l', 0) // 2,
            d.get('o', 0) // 2,
            d.get('n', 0)
        )