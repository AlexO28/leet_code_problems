# You are given an integer array nums.
# A special triplet is defined as a triplet of indices (i, j, k) such that:
# 0 <= i < j < k < n, where n = nums.length
# nums[i] == nums[j] * 2
# nums[k] == nums[j] * 2
# Return the total number of special triplets in the array.
# Since the answer may be large, return it modulo 109 + 7.
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        freq_prev = {}
        freq_next = {}
        for num in nums:
            if num in freq_next:
                freq_next[num] += 1
            else:
                freq_next[num] = 1
        res = 0
        MOD = 10**9 + 7
        for num in nums:
            if freq_next[num] == 1:
                del freq_next[num]
            else:
                freq_next[num] -= 1
            double_num = 2 * num
            if (double_num in freq_prev) and (double_num in freq_next):
                res = (res + freq_prev[double_num] * freq_next[double_num]) % MOD
            if num in freq_prev:
                freq_prev[num] += 1
            else:
                freq_prev[num] = 1
        return res
