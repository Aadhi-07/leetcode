class Solution:
    def majorityElement(self, nums):
        c = 0
        
        for x in nums:
            if c == 0:
                ans = x
            
            if x == ans:
                c += 1
            else:
                c -= 1
        
        return ans