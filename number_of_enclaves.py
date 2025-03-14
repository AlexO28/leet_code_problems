# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.d_row = [-1, 0, 1, 0]
        self.d_col = [0, 1, 0, -1]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (self.grid[row][col] > 0) and ((row == 0) or (row == len(grid) - 1) or (col == 0) or (col == len(grid[0]) - 1)):
                    self.search(row, col)
        return sum(value for row in self.grid for value in row)

    def search(self, row, col):
        self.grid[row][col] = 0
        for direction in range(4):
            new_row = row + self.d_row[direction]
            new_col = col + self.d_col[direction]
            if (new_row >= 0) and (new_row < len(self.grid)) and (new_col >= 0) and (new_col < len(self.grid[0])) and (self.grid[new_row][new_col] > 0):
                self.search(new_row, new_col)
