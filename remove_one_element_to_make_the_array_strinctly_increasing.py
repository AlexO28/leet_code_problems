# Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.
# The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).
from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return True
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            found = False
            for j in range(1, len(temp)):
                if temp[j] <= temp[j - 1]:
                    found = True
                    break
            if not found:
                return True
        return False
