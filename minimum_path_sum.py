# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = []
        for i in range(m):
            temp_list = []
            for j in range(n):
                temp_list.append(0)
            dp.append(temp_list)
        for i in range(m):
            for j in range(n):
                if (i == 0) and (j == 0):
                    dp[i][j] = grid[i][j]
                    continue
                if i == 0:
                    dp[0][j] = dp[0][j-1] + grid[0][j]
                elif j == 0:
                    dp[i][0] = dp[i-1][0] + grid[i][0]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]
