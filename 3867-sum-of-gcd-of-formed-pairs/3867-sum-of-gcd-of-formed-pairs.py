class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        prefix = []
        mx = 0

        # Build prefixGcd
        for x in nums:
            if x > mx:
                mx = x
            prefix.append(gcd(x, mx))

        # Sort
        prefix.sort()

        # Pair smallest with largest
        left = 0
        right = len(prefix) - 1
        ans = 0

        while left < right:
            ans += gcd(prefix[left], prefix[right])
            left += 1
            right -= 1

        return ans