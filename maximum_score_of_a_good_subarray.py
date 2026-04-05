# You are given an array of integers nums (0-indexed) and an integer k.
# The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.
# Return the maximum possible score of a good subarray
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = [-1] * len(nums)
        right = [len(nums)] * len(nums)
        stk = []
        for i, v in enumerate(nums):
            while stk and nums[stk[-1]] >= v:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(len(nums) - 1, -1, -1):
            v = nums[i]
            while stk and nums[stk[-1]] > v:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        ans = 0
        for i, v in enumerate(nums):
            if left[i] + 1 <= k <= right[i] - 1:
                ans = max(ans, v * (right[i] - left[i] - 1))
        return ans
