# You are given a 0-indexed integer array nums of length n.
# nums contains a valid split at index i if the following are true:
# The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
# There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        summa = sum(nums)
        cursum = 0
        res = 0
        for j in range(len(nums)-1):
            cursum += nums[j]
            if cursum >= summa - cursum:
                res += 1
        return res
