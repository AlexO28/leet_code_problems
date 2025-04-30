# Given an array nums of integers, return how many of them contain an even number of digits.
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if len(str(num)) % 2 == 0])
