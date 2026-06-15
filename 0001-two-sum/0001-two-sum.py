class Solution:
    def twoSum(self, nums, target):
        mp = {}
        
        for i, x in enumerate(nums):
            y = target - x
            
            if y in mp:
                return [mp[y], i]
            
            mp[x] = i