# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.
import math
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        freq_dict = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                num = nums[i]*nums[j]
                if num in freq_dict:
                    freq_dict[num] += 1
                else:
                    freq_dict[num] = 1
        res = 0
        for val in (freq_dict.values()):
            if val > 1:
                res += math.comb(val, 2)
        return res * 8
