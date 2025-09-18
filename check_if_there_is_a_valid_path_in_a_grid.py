# You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:
# 1 which means a street connecting the left cell and the right cell.
# 2 which means a street connecting the upper cell and the lower cell.
# 3 which means a street connecting the left cell and the lower cell.
# 4 which means a street connecting the right cell and the lower cell.
# 5 which means a street connecting the left cell and the upper cell.
# 6 which means a street connecting the right cell and the upper cell.
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        prod = len(grid[0]) * len(grid)
        self.parent = list(range(prod))
        self.grid = grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                street_type = self.grid[row][col]
                if street_type == 1:
                    self.connect_left(row, col)
                    self.connect_right(row, col)
                elif street_type == 2:
                    self.connect_up(row, col)
                    self.connect_down(row, col)
                elif street_type == 3:
                    self.connect_left(row, col)
                    self.connect_down(row, col)
                elif street_type == 4:
                    self.connect_right(row, col)
                    self.connect_down(row, col)
                elif street_type == 5:
                    self.connect_left(row, col)
                    self.connect_up(row, col)
                else:
                    self.connect_right(row, col)
                    self.connect_up(row, col)
        start_root = self.find(0)
        end_root = self.find(prod - 1)
        return start_root == end_root

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def connect_left(self, row, col):
        if col > 0 and self.grid[row][col - 1] in (1, 4, 6):
            current_root = self.find(row * len(self.grid[0]) + col)
            left_root = self.find(row * len(self.grid[0]) + col - 1)
            self.parent[current_root] = left_root

    def connect_right(self, row, col):
        if col < len(self.grid[0]) - 1 and self.grid[row][col + 1] in (1, 3, 5):
            current_root = self.find(row * len(self.grid[0]) + col)
            right_root = self.find(row * len(self.grid[0]) + col + 1)
            self.parent[current_root] = right_root

    def connect_up(self, row, col):
        if row > 0 and self.grid[row - 1][col] in (2, 3, 4):
            current_root = self.find(row * len(self.grid[0]) + col)
            up_root = self.find((row - 1) * len(self.grid[0]) + col)
            self.parent[current_root] = up_root

    def connect_down(self, row, col):
        if row < len(self.grid) - 1 and self.grid[row + 1][col] in (2, 5, 6):
            current_root = self.find(row * len(self.grid[0]) + col)
            down_root = self.find((row + 1) * len(self.grid[0]) + col)
            self.parent[current_root] = down_root
