# You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.
# You may perform only the following operations:
# Reverse the entire array.
# Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.
# Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.
from math import inf
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        zero = nums.index(0)
        res = inf
        if self.check(1, nums, zero):
            res = min(res, zero)
            res = min(res, len(nums) - zero + 2)
        if self.check(-1, nums, zero):
            res = min(res, zero + 2)
            res = min(res, len(nums) - zero)
        return -1 if res == inf else res

    def check(self, step, nums, zero):
        prev = zero
        for i in range(1, len(nums)):
            curr = (prev + step) % len(nums)
            if nums[prev] > nums[curr]:
                return False
            prev = curr
        return True
