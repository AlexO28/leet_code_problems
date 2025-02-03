# You are given an array of integers nums. Return the length of the longest 
# subarray
#  of nums which is either 
# strictly increasing
#  or 
# strictly decreasing
# .
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        max_len = 1
        regime = 0
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if regime > 0:
                    cur_len += 1
                else:
                    max_len = max(max_len, cur_len)
                    cur_len = 2
                    regime = 1
            elif nums[i] < nums[i-1]:
                if regime < 0:
                    cur_len += 1
                else:
                    max_len = max(max_len, cur_len)
                    cur_len = 2
                    regime = -1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
                regime = 0
        return max(max_len, cur_len)
