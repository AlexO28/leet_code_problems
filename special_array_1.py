# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(1, len(nums)):
            if (nums[i-1] + nums[i]) % 2 == 0:
                return False
        return True
