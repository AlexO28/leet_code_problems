# You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).
# The total value of an island is the sum of the values of all cells in the island.
# Return the number of islands with a total value divisible by k.
from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    if self.search(grid, i, j) % k == 0:
                        res += 1
        return res

    def search(self, grid, i, j):
        res = grid[i][j]
        grid[i][j] = -1
        if i > 0:
            if grid[i - 1][j] > 0:
                res += self.search(grid, i - 1, j)
        if j > 0:
            if grid[i][j - 1] > 0:
                res += self.search(grid, i, j - 1)
        if i < len(grid) - 1:
            if grid[i + 1][j] > 0:
                res += self.search(grid, i + 1, j)
        if j < len(grid[0]) - 1:
            if grid[i][j + 1] > 0:
                res += self.search(grid, i, j + 1)
        return res
