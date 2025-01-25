# An array is squareful if the sum of every pair of adjacent elements is a perfect square.
# Given an integer array nums, return the number of permutations of nums that are squareful.
# Two permutations perm1 and perm2 are different if there is some index i such that perm1[i] != perm2[i].
from math import sqrt
from collections import Counter
from math import factorial
from typing import List


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        dp = [[0] * len(nums) for i in range(1 << len(nums))]
        for j in range(len(nums)):
            dp[1 << j][j] = 1
        for mask in range(1 << len(nums)):
            for end_pos in range(len(nums)):
                if mask >> end_pos & 1:
                    for next_pos in range(len(nums)):
                        if mask >> next_pos & 1 and next_pos != end_pos:
                            potential_square = nums[end_pos] + nums[next_pos]
                            if int(sqrt(potential_square)) ** 2 == potential_square:
                                dp[mask][end_pos] += dp[mask ^ (1 << end_pos)][next_pos]
        result = sum(dp[(1 << len(nums)) - 1][j] for j in range(len(nums)))
        vals = Counter(nums).values()
        for val in vals:
            result //= factorial(val)      
        return result
