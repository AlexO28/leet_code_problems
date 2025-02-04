# Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
# A subarray is defined as a contiguous sequence of numbers in an array.
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_sum += nums[i]
            else:
                max_sum = max(max_sum, cur_sum)
                cur_sum = nums[i]
        return max(max_sum, cur_sum)
