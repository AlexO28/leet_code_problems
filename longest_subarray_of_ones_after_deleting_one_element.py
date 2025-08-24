# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        zero_pos = None
        start = 0
        end = 0
        cur_sum = 0
        res = 0
        end = 0
        while end < len(nums):
            if nums[end] == 1:
                cur_sum += 1
                end += 1
            else:
                if zero_pos is None:
                    zero_pos = end
                    end += 1
                else:
                    res = max(cur_sum, res)
                    if start <= zero_pos:
                        start = zero_pos + 1
                    else:
                        start = end
                    end = start
                    zero_pos = None
                    cur_sum = 0
        if zero_pos is None:
            return max(cur_sum - 1, res)
        else:
            return max(cur_sum, res)
