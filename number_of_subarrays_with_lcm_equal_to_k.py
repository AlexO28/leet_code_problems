# Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.
from math import lcm


class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            prevnum = 1
            for j in range(i, len(nums)):
                prevnum = lcm(prevnum, nums[j])
                if prevnum > k:
                    break
                elif prevnum == k:
                    res += 1
        return res
