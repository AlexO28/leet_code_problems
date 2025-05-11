# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        else:
            for i in range(len(arr)-2):
                if (arr[i] % 2 == 1) and (arr[i+1] % 2 == 1) and (arr[i+2] % 2 == 1):
                    return True
            return False
