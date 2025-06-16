# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        else:
            res = [-1]
            max_val = arr[-1]
            for j in range(len(arr)-2, -1, -1):
                res.append(max_val)
                max_val = max(max_val, arr[j])
            return res[::-1]
