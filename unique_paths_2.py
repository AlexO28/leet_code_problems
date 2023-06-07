# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = []
        for i in range(m):
            temp_list = []
            for j in range(n):
                temp_list.append(0)
            dp.append(temp_list)
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(m):
            for j in range(n):
                if (i == 0) and (j == 0):
                    dp[i][j] = 1
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                if (i > 0) and (j > 0):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i > 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[m-1][n-1]
