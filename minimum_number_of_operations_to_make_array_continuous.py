# You are given an integer array nums. In one operation, you can replace any element in nums with any integer.
# nums is considered continuous if both of the following conditions are fulfilled:
# All elements in nums are unique.
# The difference between the maximum element and the minimum element in nums equals nums.length - 1.
# Return the minimum number of operations to make nums continuous.
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        j = 0
        nums = sorted(set(nums))
        for i, v in enumerate(nums):
            while j < len(nums) and nums[j] - v <= n - 1:
                j += 1
            res = min(res, n - (j - i))
        return res
