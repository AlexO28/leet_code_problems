# Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        i = 0
        res = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] < target:
                    res += 1
                    j += 1
                else:
                    break
            i += 1
        return res
