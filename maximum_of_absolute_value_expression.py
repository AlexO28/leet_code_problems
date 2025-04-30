# Given two arrays of integers with equal lengths, return the maximum value of:
# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
# where the maximum is taken over all 0 <= i, j < arr1.length.
from math import inf
from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        for dir1, dir2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            max_val = -inf
            min_val = inf
            for i in range(len(arr1)):
                cur_val = dir1 * arr1[i] + dir2 * arr2[i] + i
                max_val = max(max_val, cur_val)
                min_val = min(min_val, cur_val)
            res = max(res, max_val - min_val)
        return res
