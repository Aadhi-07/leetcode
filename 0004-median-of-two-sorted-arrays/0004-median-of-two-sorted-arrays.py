class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        l, r = 0, m

        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i

            a1 = float('-inf') if i == 0 else nums1[i - 1]
            a2 = float('inf') if i == m else nums1[i]

            b1 = float('-inf') if j == 0 else nums2[j - 1]
            b2 = float('inf') if j == n else nums2[j]

            if a1 <= b2 and b1 <= a2:
                if (m + n) % 2:
                    return float(max(a1, b1))
                return (max(a1, b1) + min(a2, b2)) / 2.0

            elif a1 > b2:
                r = i - 1
            else:
                l = i + 1