# You are given a 0-indexed integer array nums.
# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.
# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res
