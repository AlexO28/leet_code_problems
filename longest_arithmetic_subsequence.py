# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
# Note that:
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp_table = [[1]*1001 for i in range(len(nums))]
        max_length = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff_index = nums[i] - nums[j] + 500
                dp_table[i][diff_index] = max(dp_table[i][diff_index], dp_table[j][diff_index] + 1)
                max_length = max(max_length, dp_table[i][diff_index])
        return max_length
