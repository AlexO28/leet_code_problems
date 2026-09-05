# You are given an integer array nums of length n and an integer numSlots such that 2 * numSlots >= n. There are numSlots slots numbered from 1 to numSlots.
# You have to place all n integers into the slots such that each slot contains at most two numbers. The AND sum of a given placement is the sum of the bitwise AND of every number with its respective slot number.
# Return the maximum possible AND sum of nums given numSlots slots.
from typing import List


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        m = numSlots << 1
        two_to_m = 1 << m
        f = [0] * two_to_m
        for i in range(two_to_m):
            cnt = i.bit_count()
            if cnt > len(nums):
                continue
            for j in range(m):
                if i >> j & 1:
                    f[i] = max(f[i], f[i ^ (1 << j)] + (nums[cnt - 1] & (j // 2 + 1)))
        return max(f)
