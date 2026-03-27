# You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.
# You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:
# Choose one integer x from either the start or the end of the array nums.
# Add multipliers[i] * x to your score.
# Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
# Remove x from nums.
# Return the maximum score after performing m operations.
from typing import List
from functools import cache


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        self.nums = nums
        self.multipliers = multipliers
        return self.f(0, len(nums) - 1, 0)

    @cache
    def f(self, i, j, k):
        if (k >= len(self.multipliers)) or (i >= len(self.nums)) or (j < 0):
            return 0
        a = self.f(i + 1, j, k + 1) + self.nums[i] * self.multipliers[k]
        b = self.f(i, j - 1, k + 1) + self.nums[j] * self.multipliers[k]
        return max(a, b)
