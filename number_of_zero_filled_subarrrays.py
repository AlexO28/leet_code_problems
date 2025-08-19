# Given an integer array nums, return the number of subarrays filled with 0.
# A subarray is a contiguous non-empty sequence of elements within an array.
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        number_of_zeros = 0
        current_number_of_zeros = 0
        for elem in nums[::-1]:
            if elem == 0:
                current_number_of_zeros += 1
                number_of_zeros += current_number_of_zeros
            else:
                current_number_of_zeros = 0
        return number_of_zeros
