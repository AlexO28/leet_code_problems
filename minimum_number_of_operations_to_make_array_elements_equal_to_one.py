# You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:
# Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
# Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.
# The gcd of two integers is the greatest common divisor of the two integers.
from typing import List
from math import gcd


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones_count = nums.count(1)
        if ones_count > 0:
            return len(nums) - ones_count
        min_length = len(nums) + 1
        for start_idx in range(len(nums)):
            current_gcd = 0
            for end_idx in range(start_idx, len(nums)):
                current_gcd = gcd(current_gcd, nums[end_idx])
                if current_gcd == 1:
                    subarray_length = end_idx - start_idx + 1
                    min_length = min(min_length, subarray_length)
                    break
        if min_length > len(nums):
            return -1
        else:
            return len(nums) + min_length - 2
