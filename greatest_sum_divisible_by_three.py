# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.
from typing import List
from math import inf


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        max_sums = [0, -inf, -inf]
        for num in nums:
            new_max_sums = max_sums.copy()
            for remainder in range(3):
                new_max_sums[remainder] = max(
                    max_sums[remainder], max_sums[(remainder - num) % 3] + num
                )
            max_sums = new_max_sums
        return max_sums[0]
