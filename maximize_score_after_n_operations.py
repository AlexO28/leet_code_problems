# You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.
# In the ith operation (1-indexed), you will:
# Choose two elements, x and y.
# Receive a score of i * gcd(x, y).
# Remove x and y from nums.
# Return the maximum score you can receive after performing n operations.
# The function gcd(x, y) is the greatest common divisor of x and y.
from typing import List
from math import gcd


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        upper = 1 << len(nums)
        f = [0] * upper
        g = [[0] * len(nums) for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                g[i][j] = gcd(nums[i], nums[j])
        for k in range(upper):
            cnt = k.bit_count()
            if cnt % 2 == 0:
                for i in range(len(nums)):
                    if k >> i & 1:
                        for j in range(i + 1, len(nums)):
                            if k >> j & 1:
                                f[k] = max(
                                    f[k],
                                    f[k ^ (1 << i) ^ (1 << j)] + cnt // 2 * g[i][j],
                                )
        return f[-1]
