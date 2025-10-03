# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.
# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.
from collections import deque
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        indices_deque = deque([0])
        dp = [0] * len(nums)
        max_sum = float("-inf")
        for current_index, current_value in enumerate(nums):
            while indices_deque and current_index - indices_deque[0] > k:
                indices_deque.popleft()
            dp[current_index] = max(0, dp[indices_deque[0]]) + current_value
            max_sum = max(max_sum, dp[current_index])
            while indices_deque and dp[indices_deque[-1]] <= dp[current_index]:
                indices_deque.pop()
            indices_deque.append(current_index)
        return max_sum
