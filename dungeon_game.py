# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

# Return the knight's minimum initial health so that he can rescue the princess.

import numpy as np


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = np.zeros([m, n])
        for i in range(m):
            for j in range(n):
                if (i>0) and (j>0):
                    dp[m-i-1][n-j-1] = max(min(dp[m-i][n-j-1], dp[m-i-1][n-j]) -
                                           dungeon[m-i-1][n-j-1], 0)
                elif (j==0) and (i>0):
                    dp[m-i-1][n-j-1] = max(dp[m-i][n-j-1] -
                                           dungeon[m-i-1][n-j-1], 0)
                elif (i==0) and (j>0):
                    dp[m-i-1][n-j-1] = max(dp[m-i-1][n-j] -
                                           dungeon[m-i-1][n-j-1], 0)
                else:
                    dp[m-i-1][n-j-1] = max(-dungeon[m-i-1][n-j-1], 0)
        return round(dp[0][0]) + 1
