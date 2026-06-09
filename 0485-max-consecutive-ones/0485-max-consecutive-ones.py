class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        ans = 0
        
        for x in nums:
            if x == 1:
                c += 1
                if c > ans:
                    ans = c
            else:
                c = 0
        
        return ans

        