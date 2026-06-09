class Solution:
    def smallerNumbersThanCurrent(self, nums):
        mp = {}
        
        for i, x in enumerate(sorted(nums)):
            if x not in mp:
                mp[x] = i
        
        return [mp[x] for x in nums]