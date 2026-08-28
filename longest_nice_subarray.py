# You are given an array nums consisting of positive integers.
# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
# Return the length of the longest nice subarray.
# A subarray is a contiguous part of an array.
# Note that subarrays of length 1 are always considered nice.
from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        max_len = 1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                found = False
                for k in range(i, j):
                    if nums[k] & nums[j] != 0:
                        found = True
                        break
                if not found:
                    max_len = max(max_len, j - i + 1)
                else:
                    break
        return max_len
