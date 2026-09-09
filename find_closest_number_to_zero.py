# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.
from typing import List
from math import inf


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        val = inf
        for num in nums:
            if abs(num) < abs(val):
                val = num
            elif abs(num) == abs(val):
                val = max(val, num)
        return val
