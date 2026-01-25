# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
# Return the minimum possible difference.
from typing import List
from math import inf


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = inf
        for j in range(len(nums) - k + 1):
            min_diff = min(min_diff, nums[k + j - 1] - nums[j])
        return min_diff
