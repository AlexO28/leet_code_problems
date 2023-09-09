# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

import numpy as np


class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = np.zeros(target + 1)
        dp[0] = 1
        for t in range(1, target+1):
            for num in nums:
                if t >= num:
                    dp[t] += dp[t-num]
        return int(dp[-1])
