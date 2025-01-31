# You are given a binary array nums (0-indexed).
# We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).
# For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
# Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        if len(nums) == 1:
            return nums[0] % 5 == 0
        num = nums[0]
        res = []
        res.append(num % 5 == 0)
        for j in range(1, len(nums)):
            num = 2*num + nums[j]
            res.append(num % 5 == 0)
        return res
