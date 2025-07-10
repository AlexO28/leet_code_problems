# Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.
# In case of a tie, return the minimum such integer.
# Notice that the answer is not neccesarilly a number from arr.
import numpy as np
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        self.arr = arr
        self.target = target
        return self.ternary_search(0, max(arr))

    def ternary_search(self, left, right):
        if right - left <= 2:
            val_1 = self.calculateCloseness(left)
            val_2 = self.calculateCloseness(left + 1)
            val_3 = self.calculateCloseness(left + 2)
            max_val = max(val_1, val_2, val_3)
            if val_1 == max_val:
                return left
            elif val_2 == max_val:
                return left + 1
            else:
                return left + 2
        left_third = int(np.floor((2 * left + right) / 3))
        right_third = int(np.ceil((left + 2 * right) / 3))
        if self.calculateCloseness(left_third) < self.calculateCloseness(right_third):
            return self.ternary_search(left_third, right)
        else:
            return self.ternary_search(left, right_third)

    def calculateCloseness(self, value):
        res = 0
        for j in range(len(self.arr)):
            res += min(self.arr[j], value)
        return -abs(res - self.target)
