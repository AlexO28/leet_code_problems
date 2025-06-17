# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
# Return the number of closed islands.
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.directions = (-1, 0, 1, 0, -1)
        res = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    res += self.search(i, j)
        return res

    def search(self, row, col):
        if (0 < row < len(self.grid) - 1) and (0 < col < len(self.grid[0]) - 1):
            result = 1
        else:
            result = 0
        self.grid[row][col] = 1
        for direction in range(4):
            new_row = row + self.directions[direction]
            new_col = col + self.directions[direction + 1]
            if (
                (0 <= new_row < len(self.grid))
                and (0 <= new_col < len(self.grid[0]))
                and (self.grid[new_row][new_col] == 0)
            ):
                result &= self.search(new_row, new_col)
        return result
