# Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.
# Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            max_element = 0
            for j in range(i, max(0, i - k), -1):
                max_element = max(max_element, arr[j - 1])
                dp[i] = max(dp[i], dp[j - 1] + max_element * (i - j + 1))
        return dp[-1]
