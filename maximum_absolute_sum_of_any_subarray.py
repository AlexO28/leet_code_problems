# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
# Return the maximum absolute sum of any (possibly empty) subarray of nums.
# Note that abs(x) is defined as follows:
# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        f_max = 0
        g_min = 0
        res = 0
        for num in nums:
            f_max = max(f_max, 0) + num
            g_min = min(g_min, 0) + num
            res = max(res, f_max, abs(g_min))
        return res
