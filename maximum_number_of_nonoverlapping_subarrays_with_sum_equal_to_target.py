# Given an array nums and an integer target, return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.
from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        result = 0
        index = 0
        while index < len(nums):
            current_sum = 0
            seen_prefix_sums = {0}
            while index < len(nums):
                current_sum += nums[index]
                if current_sum - target in seen_prefix_sums:
                    result += 1
                    break
                index += 1
                seen_prefix_sums.add(current_sum)
            index += 1
        return result
