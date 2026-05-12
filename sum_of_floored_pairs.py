# Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs of indices 0 <= i, j < nums.length in the array. Since the answer may be too large, return it modulo 109 + 7.
# The floor() function returns the integer part of the division.
from typing import List
from collections import Counter


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mx = max(nums)
        s = [0] * (mx + 1)
        for i in range(1, mx + 1):
            s[i] = s[i - 1] + cnt[i]
        ans = 0
        for y in range(1, mx + 1):
            if cnt[y]:
                d = 1
                while d * y <= mx:
                    ans = (
                        ans + (cnt[y] * d * (s[min(mx, d * y + y - 1)] - s[d * y - 1]))
                    ) % 1000000007
                    d += 1
        return ans
