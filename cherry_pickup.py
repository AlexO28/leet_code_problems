# You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.
# 0 means the cell is empty, so you can pass through,
# 1 means the cell contains a cherry that you can pick up and pass through, or
# -1 means the cell contains a thorn that blocks your way.
# Return the maximum number of cherries you can collect by following the rules below:
# Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
# After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
# When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
# If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if grid[0][0] == -1:
            return 0
        if len(grid) == 1:
            if grid[0][0] > 0:
                return 1
            else:
                return 0
        dp = [[[-inf] * len(grid) for i in range(len(grid))] for j in range(2*len(grid) - 1)]
        dp[0][0][0] = grid[0][0]
        for k in range(1, 2*len(grid) - 1):
            for i1 in range(len(grid)):
                for i2 in range(len(grid)):
                    j1 = k - i1
                    j2 = k - i2
                    if (not 0 <= j1 < len(grid) or not 0 <= j2 < len(grid)
                        or grid[i1][j1] == -1 or grid[i2][j2] == -1):
                        continue
                    if i1 == i2:
                        t = grid[i1][j1]
                    else:
                        t = grid[i1][j1] + grid[i2][j2]
                    for x1 in range(i1 - 1, i1 + 1):
                        for x2 in range(i2 - 1, i2 + 1):
                            if x1 >= 0 and x2 >= 0:
                                dp[k][i1][i2] = max(dp[k][i1][i2], dp[k - 1][x1][x2] + t)
        return max(0, dp[-1][-1][-1])
