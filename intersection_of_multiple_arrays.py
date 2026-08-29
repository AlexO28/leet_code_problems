# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        for j in range(len(nums)):
            if j == 0:
                res = set(nums[0])
            else:
                res &= set(nums[j])
        res = list(res)
        res.sort()
        return res
