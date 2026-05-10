# The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.
# For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
# Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.
# Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.
# A subarray is a contiguous part of an array.
from typing import List
from itertools import accumulate


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = -1
        left = [-1] * len(nums)
        right = [len(nums)] * len(nums)
        stk = []
        for i, x in enumerate(nums):
            while stk and nums[stk[-1]] >= x:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(len(nums) - 1, -1, -1):
            while stk and nums[stk[-1]] > nums[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        s = list(accumulate(nums, initial=0))
        return (
            max((s[right[i]] - s[left[i] + 1]) * x for i, x in enumerate(nums))
            % 1000000007
        )
