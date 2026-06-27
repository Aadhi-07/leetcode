class Solution(object):
    def maxSubArray(self, nums):
        cur = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            ans = max(ans, cur)

        return ans