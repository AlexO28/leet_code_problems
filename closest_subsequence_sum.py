# You are given an integer array nums and an integer goal.
# You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).
# Return the minimum possible value of abs(sum - goal).
# Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.
from typing import List
from math import inf
from bisect import bisect_left


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n_half = len(nums) // 2
        left = set()
        right = set()
        self.getSubSeqSum(0, 0, nums[:n_half], left)
        self.getSubSeqSum(0, 0, nums[n_half:], right)
        result = inf
        right = sorted(right)
        rl = len(right)
        for l in left:
            remaining = goal - l
            idx = bisect_left(right, remaining)
            if idx < rl:
                result = min(result, abs(remaining - right[idx]))
            if idx > 0:
                result = min(result, abs(remaining - right[idx - 1]))
        return result

    def getSubSeqSum(self, i, curr, arr, result):
        if i == len(arr):
            result.add(curr)
        else:
            self.getSubSeqSum(i + 1, curr, arr, result)
            self.getSubSeqSum(i + 1, curr + arr[i], arr, result)
