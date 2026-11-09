# Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# The greatest common divisor of an array is the largest integer that evenly divides all the array elements.
from math import gcd


class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if j == i:
                    remainder = nums[i]
                else:
                    remainder = gcd(remainder, nums[j])
                if remainder < k:
                    break
                elif remainder % k > 0:
                    break
                elif remainder == k:
                    res += 1
        return res
