# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:
# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        freq_dict = {}
        MOD = 1000000007
        for num in nums:
            val = num - int(str(num)[::-1])
            if val in freq_dict:
                freq_dict[val] += 1
            else:
                freq_dict[val] = 1
        summa = 0
        for num in freq_dict:
            if freq_dict[num] > 1:
                summa = (summa + (freq_dict[num] * (freq_dict[num] - 1)) // 2) % MOD
        return summa
