# Given a circular array nums, find the maximum absolute difference between adjacent elements.
# Note: In a circular array, the first and last elements are adjacent.
from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return abs(nums[-1] - nums[0])
        else:
            max_diff = abs(nums[-1] - nums[0])
            for j in range(1, len(nums)):
                max_diff = max(max_diff, abs(nums[j] - nums[j-1]))
            return max_diff
