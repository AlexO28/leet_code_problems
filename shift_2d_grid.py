# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
# In one shift operation:
# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid_new = [[0] * len(grid[0]) for i in range(len(grid))]
        for z in range(k):
            for i in range(len(grid)):
                for j in range(len(grid[0]) - 1):
                    grid_new[i][j + 1] = grid[i][j]
                if i < len(grid) - 1:
                    grid_new[i + 1][0] = grid[i][len(grid[0]) - 1]
            grid_new[0][0] = grid[len(grid) - 1][len(grid[0]) - 1]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    grid[i][j] = grid_new[i][j]
        return grid
