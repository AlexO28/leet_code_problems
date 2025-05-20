# Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.
# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].
# If there is no way to make arr1 strictly increasing, return -1.
from typing import List
from bisect import bisect_left
from math import inf


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = list(set(arr2))
        arr2.sort()
        arr = [-inf] + arr1 + [inf]
        min_ops = [inf] * (len(arr))
        min_ops[0] = 0
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                min_ops[i] = min_ops[i - 1]
            replacement_idx = bisect_left(arr2, arr[i])
            for replace_count in range(1, min(i, replacement_idx) + 1):
                if arr[i - replace_count - 1] < arr2[replacement_idx - replace_count]:
                    min_ops[i] = min(min_ops[i], min_ops[i - replace_count - 1] + replace_count)
        if min_ops[len(arr) - 1] == inf:
            return -1
        else:
            return min_ops[len(arr) - 1]
