# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, nums[j] - nums[i])
        return res
