# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
import numpy as np


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if (len(nums1) == 1) and (len(nums2) == 1):
            return int(nums1[0] == nums2[0])
        elif len(nums1) == 1:
            return int(nums1[0] in nums2)
        elif len(nums2) == 1:
            return int(nums2[0] in nums1)
        dp = [[0 for j in range(len(nums2))] for i in range(len(nums1))]
        if nums1[-1] == nums2[-1]:
            dp[0][0] = 1
        for i in range(1, len(nums1)):
            if nums2[-1] == nums1[-i-1]:
                dp[i][0] = 1
        for j in range(1, len(nums2)):
            if nums1[-1] == nums2[-j-1]:
                dp[0][j] = 1
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                if nums1[-i-1] == nums2[-j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        return np.max(dp)
