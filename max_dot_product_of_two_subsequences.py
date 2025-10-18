# Given two arrays nums1 and nums2.
# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[float("-inf")] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    max(0, dp[i - 1][j - 1]) + nums1[i - 1] * nums2[j - 1],
                )
        return dp[-1][-1]
