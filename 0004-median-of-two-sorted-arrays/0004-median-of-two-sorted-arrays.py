class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sn = sorted(nums1 + nums2)
        n = len(sn)
        mid = n // 2

        if n%2:
            return sn[mid]
        else :
            return (sn[mid-1]+sn[mid])/2.0