# You may recall that an array arr is a mountain array if and only if:
# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)
        return len(nums) - max(
            a + b - 1 for a, b in zip(left, right) if a > 1 and b > 1
        )
