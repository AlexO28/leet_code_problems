# Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.
# The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.
# A subarray is a contiguous part of an array.
from typing import List
from itertools import accumulate


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sums = list(accumulate(nums, initial=0))
        max_sum = 0
        max_sum_first_array = 0
        i = firstLen
        while i + secondLen - 1 < len(nums):
            max_sum_first_array = max(max_sum_first_array, prefix_sums[i] - prefix_sums[i - firstLen])
            max_sum = max(max_sum, max_sum_first_array + prefix_sums[i + secondLen] - prefix_sums[i])
            i += 1
        max_sum_second_array = 0
        i = secondLen
        while i + firstLen - 1 < len(nums):
            max_sum_second_array = max(max_sum_second_array, prefix_sums[i] - prefix_sums[i - secondLen])
            max_sum = max(max_sum, max_sum_second_array + prefix_sums[i + firstLen] - prefix_sums[i])
            i += 1
        return max_sum
