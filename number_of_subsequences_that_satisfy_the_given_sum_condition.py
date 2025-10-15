# You are given an array of integers nums and an integer target.
# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.
from typing import List
from bisect import bisect_right


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        power_of_two = [1] * len(nums)
        for i in range(1, len(nums)):
            power_of_two[i] = (power_of_two[i - 1] * 2) % MOD
        result = 0
        for left_idx, min_val in enumerate(nums):
            if min_val * 2 > target:
                break
            right_idx = bisect_right(nums, target - min_val, left_idx + 1) - 1
            subsequence_count = power_of_two[right_idx - left_idx]
            result = (result + subsequence_count) % MOD
        return result
