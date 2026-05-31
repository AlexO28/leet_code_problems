# The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.
# For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
# Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        f = [0] * (len(nums) + 1)
        g = [0] * (len(nums) + 1)
        for i, x in enumerate(nums, 1):
            f[i] = max(g[i - 1] - x, f[i - 1])
            g[i] = max(f[i - 1] + x, g[i - 1])
        return max(f[-1], g[-1])
