# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
# A subarray is a contiguous part of an array.
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq_dict = {0: 1}
        res = 0
        current_sum = 0
        for num in nums:
            current_sum = (current_sum + num) % k
            if current_sum in freq_dict:
                res += freq_dict[current_sum]
                freq_dict[current_sum] += 1
            else:
                freq_dict[current_sum] = 1
        return res
