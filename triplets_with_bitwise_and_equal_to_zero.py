# Given an integer array nums, return the number of AND triples.
# An AND triple is a triple of indices (i, j, k) such that:
# 0 <= i < nums.length
# 0 <= j < nums.length
# 0 <= k < nums.length
# nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.
from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        count_dict = {}
        for x in nums:
            for y in nums:
                z = x & y
                if z in count_dict:
                    count_dict[z] += 1
                else:
                    count_dict[z] = 1
        res = 0
        for x in count_dict:
            for y in nums:
                if x & y == 0:
                    res += count_dict[x]
        return res
