class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        cnt = [0] * (n + 1)
        
        for x in nums:
            cnt[x] += 1
        
        a = b = 0
        
        for i in range(1, n + 1):
            if cnt[i] == 2:
                a = i
            elif cnt[i] == 0:
                b = i
        
        return [a, b]