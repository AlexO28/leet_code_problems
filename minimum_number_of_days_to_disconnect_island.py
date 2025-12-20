# You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.
# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
# In one day, we are allowed to change any single land cell (1) into a water cell (0).
# Return the minimum number of days to disconnect the grid.
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        self.grid = grid
        if self.count() != 1:
            return 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    self.grid[i][j] = 0
                    if self.count() != 1:
                        return 1
                    self.grid[i][j] = 1
        return 2

    def count(self):
        cnt = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    self.search(i, j)
                    cnt += 1
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 2:
                    self.grid[i][j] = 1
        return cnt

    def search(self, i, j):
        self.grid[i][j] = 2
        for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            x = i + a
            y = j + b
            if (
                0 <= x < len(self.grid)
                and 0 <= y < len(self.grid[0])
                and self.grid[x][y] == 1
            ):
                self.search(x, y)
