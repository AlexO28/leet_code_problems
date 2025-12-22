# Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.
# Return the length of the shortest subarray to remove.
# A subarray is a contiguous subsequence of the array.
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        left = 0
        next_left = left + 1
        while next_left < len(arr) and arr[left] <= arr[next_left]:
            left = next_left
            next_left += 1
        if left == len(arr) - 1:
            return 0
        right = len(arr) - 1
        next_right = right - 1
        while right > 0 and arr[next_right] <= arr[right]:
            right = next_right
            next_right -= 1
        result = min(len(arr) - left - 1, right)
        i = 0
        j = right
        while i <= left and j < len(arr):
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
        return result
