# Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.
# Answers within 10-5 of the actual answer will be considered accepted.
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        first_index = int(len(arr) * 0.05)
        last_index = int(len(arr) * 0.95)
        res = 0
        for j in range(first_index, last_index):
            res += arr[j]
        return res / (last_index - first_index)
