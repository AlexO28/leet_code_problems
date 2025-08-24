# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        zero_pos = None
        start = 0
        end = 0
        cur_sum = 0
        res = 0
        end = 0
        while start < len(nums):
            if nums[end] == 1:
                cur_sum += 1
                end += 1
            else:
                if zero_pos is None:
                    zero_pos = end
                    cur_sum += 1
                else:
                    res = max(cur_sum, res)
                    start = zero_pos + 1
                    end = start
        return max(cur_sum, res)
