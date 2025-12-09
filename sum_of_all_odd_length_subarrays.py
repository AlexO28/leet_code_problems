# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array.
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            summa = 0
            dur = 0
            for j in range(i, len(arr)):
                summa += arr[j]
                dur += 1
                if dur % 2 == 1:
                    res += summa
        return res
