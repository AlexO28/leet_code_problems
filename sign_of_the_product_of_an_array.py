# Implement a function signFunc(x) that returns:
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        number_of_minuses = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                number_of_minuses += 1
        if number_of_minuses % 2 == 0:
            return 1
        else:
            return -1
