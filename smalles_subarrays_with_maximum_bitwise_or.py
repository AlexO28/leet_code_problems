# You are given a 0-indexed array nums of length n, consisting of non-negative integers. For each index i from 0 to n - 1, you must determine the size of the minimum sized non-empty subarray of nums starting at i (inclusive) that has the maximum possible bitwise OR.
# In other words, let Bij be the bitwise OR of the subarray nums[i...j]. You need to find the smallest subarray starting at i, such that bitwise OR of this subarray is equal to max(Bik) where i <= k <= n - 1.
# The bitwise OR of an array is the bitwise OR of all the numbers in it.
# Return an integer array answer of size n where answer[i] is the length of the minimum sized subarray starting at i with maximum bitwise OR.
# A subarray is a contiguous non-empty sequence of elements within an array.
from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        f = [-1] * 32
        for i in range(len(nums) - 1, -1, -1):
            t = 1
            for j in range(32):
                if (nums[i] >> j) & 1:
                    f[j] = i
                elif f[j] != -1:
                    t = max(t, f[j] - i + 1)
            ans[i] = t
        return ans
