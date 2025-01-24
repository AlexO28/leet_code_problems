# You are given a binary array nums and an integer k.
# A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
# Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
# A subarray is a contiguous part of an array.
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips = [0] * (len(nums) + 1)
        total_flips = 0
        flip_counter = 0     
        for j in range(len(nums)):
            flip_counter += flips[j]
            if (nums[j] + flip_counter) % 2 == 0:
                if j + k > len(nums):
                    return -1
                flips[j] += 1
                flips[j + k] -= 1              
                flip_counter += 1
                total_flips += 1
        return total_flips
