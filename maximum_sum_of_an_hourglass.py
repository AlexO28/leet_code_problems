# You are given an m x n integer matrix grid.
# We define an hourglass as a part of the matrix with the following form:
# Return the maximum sum of the elements of an hourglass.
# Note that an hourglass cannot be rotated and must be entirely contained within the matrix.
class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        res = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                res = max(
                    res,
                    grid[i][j]
                    + grid[i][j + 1]
                    + grid[i][j + 2]
                    + grid[i + 1][j + 1]
                    + grid[i + 2][j]
                    + grid[i + 2][j + 1]
                    + grid[i + 2][j + 2],
                )
        return res
