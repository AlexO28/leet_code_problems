# Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.
# A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        prevIndex = {}
        dp = [0] * len(arr)
        ans = 0
        for i in range(len(arr)):
            prevNum = arr[i] - difference
            if prevNum in prevIndex:
                dp[i] = dp[prevIndex[prevNum]] + 1
            else:
                dp[i] = 1
            prevIndex[arr[i]] = i
            ans = max(ans, dp[i])
        return ans
