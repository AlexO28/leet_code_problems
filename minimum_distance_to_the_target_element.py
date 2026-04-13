# Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.
# Return abs(i - start).
# It is guaranteed that target exists in nums.
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target:
            return 0
        delta = 1
        while True:
            next_ind = start + delta
            if next_ind < len(nums):
                if nums[next_ind] == target:
                    return delta
            next_ind = start - delta
            if next_ind >= 0:
                if nums[next_ind] == target:
                    return delta
            delta += 1
