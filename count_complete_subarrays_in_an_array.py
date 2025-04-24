# You are given an array nums consisting of positive integers.
# We call a subarray of an array complete if the following condition is satisfied:
# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.
# A subarray is a contiguous non-empty part of an array.
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(list(set(nums)))
        if k == len(nums):
            return 1
        freq_dict = {}
        res = 0
        length = len(nums)
        start_index = 0
        for end_index in range(len(nums)):
            if nums[end_index] in freq_dict:
                freq_dict[nums[end_index]] += 1
            else:
                freq_dict[nums[end_index]] = 1
            while len(freq_dict) == k:
                res += length - end_index
                freq_dict[nums[start_index]] -= 1
                if freq_dict[nums[start_index]] == 0:
                    del freq_dict[nums[start_index]]
                start_index += 1
        return res
