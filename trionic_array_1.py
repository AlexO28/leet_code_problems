# You are given an integer array nums of length n.
# An array is trionic if there exist indices 0 < p < q < n − 1 such that:
# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.
from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        j = 1
        found = False
        while j < len(nums):
            if nums[j] <= nums[j - 1]:
                found = True
                break
            else:
                j += 1
        if (not found) or (j == len(nums)) or (j == 1):
            return False
        found = False
        while j < len(nums):
            if nums[j] >= nums[j - 1]:
                found = True
                break
            else:
                j += 1
        if (not found) or (j == len(nums)):
            return False
        while j < len(nums):
            if nums[j] <= nums[j - 1]:
                return False
            else:
                j += 1
        return True
