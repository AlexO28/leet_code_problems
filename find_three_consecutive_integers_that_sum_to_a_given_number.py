# Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.
from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = (num - 3) // 3
        nums = [x, x + 1, x + 2]
        if sum(nums) == num:
            return nums
        else:
            return []
