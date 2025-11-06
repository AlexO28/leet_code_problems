# Given the array houses where houses[i] is the location of the ith house along a street and an integer k, allocate k mailboxes in the street.
# Return the minimum total distance between each house and its nearest mailbox.
# The test cases are generated so that the answer fits in a 32-bit integer.
from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        cost = [[0] * len(houses) for i in range(len(houses))]
        for i in range(len(houses) - 2, -1, -1):
            for j in range(i + 1, len(houses)):
                cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]
        dp = [[float("inf")] * (k + 1) for _ in range(len(houses))]
        for i in range(len(houses)):
            dp[i][1] = cost[0][i]
            for j in range(2, min(k + 1, i + 2)):
                for p in range(i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p + 1][i])
        return dp[-1][k]
