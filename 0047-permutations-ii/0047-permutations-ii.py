class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        used = [False] * len(nums)

        def bt(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])

                bt(path)

                path.pop()
                used[i] = False

        bt([])
        return res