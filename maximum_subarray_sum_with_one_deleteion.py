# Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.
# Note that the subarray needs to be non-empty after deleting one element.
from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        max_sum_left = [0] * (len(arr))
        max_sum_right = [0] * (len(arr))
        current_sum = 0
        for i, value in enumerate(arr):
            current_sum = max(current_sum, 0) + value
            max_sum_left[i] = current_sum
        current_sum = 0
        for i in range(len(arr) - 1, -1, -1):
            current_sum = max(current_sum, 0) + arr[i]
            max_sum_right[i] = current_sum
        max_sum = max(max_sum_left)
        for i in range(1, len(arr) - 1):
            max_sum = max(max_sum, max_sum_left[i - 1] + max_sum_right[i + 1])
        return max_sum
