class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        left = []
        mid = ""

        for ch in sorted(freq.keys()):
            left.append(ch * (freq[ch] // 2))
            if freq[ch] % 2 == 1:
                mid = ch

        left = "".join(left)
        return left + mid + left[::-1]