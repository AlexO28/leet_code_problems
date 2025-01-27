# There are n piles of stones arranged in a row. The ith pile has stones[i] stones.
# A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.
# Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.
from typing import List
from itertools import accumulate
from math import inf


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if (len(stones) - 1) % (k - 1) > 0:
            return -1
        else:
            prefix_sum = list(accumulate(stones, initial=0))
            dp = [[[inf]*(k + 1) for i in range(len(stones)+1)] for j in range(len(stones)+1)]
            for i in range(len(stones)+1):
                dp[i][i][1] = 0
            for x in range(2, len(stones)+1):
                for i in range(1, len(stones)-x+2):
                    j = i + x - 1
                    for y in range(1, k+1):
                        for z in range(i, j):
                            dp[i][j][y] = min(dp[i][j][y], dp[i][z][1] + dp[z+1][j][y-1])
                    dp[i][j][1] = dp[i][j][k] + prefix_sum[j] - prefix_sum[i-1]
            return dp[1][len(stones)][1]
