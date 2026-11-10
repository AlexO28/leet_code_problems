# You are climbing a staircase with n + 1 steps, numbered from 0 to n.
# You are also given a 1-indexed integer array costs of length n, where costs[i] is the cost of step i.
# From step i, you can jump only to step i + 1, i + 2, or i + 3. The cost of jumping from step i to step j is defined as: costs[j] + (j - i)2
# You start from step 0 with cost = 0.
# Return the minimum total cost to reach step n.
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)
        for j in range(n):
            if j == 0:
                dp[j + 1] = dp[j] + costs[j] + 1
            elif j == 1:
                dp[j + 1] = min(dp[j] + costs[j] + 1, dp[j - 1] + costs[j] + 4)
            else:
                dp[j + 1] = min(dp[j] + costs[j] + 1, dp[j - 1] + costs[j] + 4, dp[j - 2] + costs[j] + 9)
        return dp[-1]
