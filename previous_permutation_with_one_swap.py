# Given an array of positive integers arr (not necessarily distinct), return the lexicographically largest permutation that is smaller than arr, that can be made with exactly one swap. If it cannot be done, then return the same array.
# Note that a swap exchanges the positions of two numbers arr[i] and arr[j]
from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                for j in range(len(arr) - 1, i - 1, -1):
                    if (arr[j] < arr[i - 1]) and (arr[j] != arr[j - 1]):
                        arr[i - 1], arr[j] = arr[j], arr[i - 1]
                        return arr
        return arr
