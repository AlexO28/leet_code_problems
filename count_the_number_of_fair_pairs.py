# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
# A pair (i, j) is fair if:
# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper
from typing import List
from bisect import bisect_left


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        res = 0
        for start in range(len(nums) - 1):
            lower_bound = bisect_left(nums, lower - nums[start], lo = start + 1)
            upper_bound = bisect_left(nums, upper - nums[start] + 1, lo = start + 1)
            res += upper_bound - lower_bound
        return res
