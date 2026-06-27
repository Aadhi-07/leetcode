class Solution(object):
    def maximumLength(self, nums):
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        ans = 1

        for x in freq:
            if x == 1:
                c = freq[x]
                ans = max(ans, c if c % 2 else c - 1)
                continue

            cur = x
            length = 0

            while cur in freq:
                if freq[cur] >= 2:
                    length += 2
                    cur = cur * cur
                else:
                    length += 1
                    break

            if length % 2 == 0:
                length -= 1

            ans = max(ans, length)

        return ans