# You are given an integer array nums of length n.
# A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:
# Left subarray contains indices [0, i].
# Right subarray contains indices [i + 1, n - 1].
# Return the number of partitions where the difference between the sum of the left and right subarrays is even.
from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        summa_right = sum(nums)
        summa_left = 0
        res = 0
        for i in range(len(nums)-1):
            summa_left += nums[i]
            summa_right -= nums[i]
            if abs(summa_right - summa_left) % 2 == 0:
                res += 1
        return res
