class Solution:
    def isDigitorialPermutation(self, n):
        s = sorted(str(n))
        for x in ["1", "2", "145", "40585"]:
            if len(x) == len(s) and sorted(x) == s:
                return True
        return False