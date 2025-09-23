# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if len(nums) > 1:
            summa = nums[0]
            min_sum = summa
            for j in range(1, len(nums)):
                summa += nums[j]
                min_sum = min(min_sum, summa)
            if min_sum >= 0:
                return 1
            else:
                return 1 - min_sum
        else:
            if nums[0] >= 0:
                return 1
            else:
                return 1 - nums[0]
