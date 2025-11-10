# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return True
        else:
            arr.sort()
            diff = arr[1] - arr[0]
            for j in range(2, len(arr)):
                if arr[j] - arr[j - 1] != diff:
                    return False
            return True
