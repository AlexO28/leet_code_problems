# You are given two positive integer arrays nums1 and nums2, both of length n.
# The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).
# You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.
# Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.
from typing import List
from math import inf
from bisect import bisect_left


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 1000000007
        nums = sorted(nums1)
        s = sum(abs(a - b) for a, b in zip(nums1, nums2)) % MOD
        mx = 0
        for a, b in zip(nums1, nums2):
            d1 = abs(a - b)
            d2 = inf
            i = bisect_left(nums, b)
            if i < len(nums):
                d2 = min(d2, abs(nums[i] - b))
            if i > 0:
                d2 = min(d2, abs(nums[i - 1] - b))
            mx = max(mx, d1 - d2)
        return (s - mx) % MOD
