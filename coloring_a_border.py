# You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.
# Two squares are called adjacent if they are next to each other in any of the 4 directions.
# Two squares belong to the same connected component if they have the same color and they are adjacent.
# The border of a connected component is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).
# You should color the border of the connected component that contains the square grid[row][col] with color.
# Return the final grid.
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        self.grid = grid
        self.component = {}
        self.formComponent(row, col, grid[row][col])
        border = self.findBorder(grid[row][col])
        for i, j in border:
            self.grid[i][j] = color
        return self.grid

    def formComponent(self, row, col, color):
        code = str(row) + "_" + str(col)
        self.component[code] = 1
        if row > 0:
            if self.grid[row-1][col] == color:
                code = str(row-1) + "_" + str(col)
                if code not in self.component:
                    self.formComponent(row-1, col, color)
        if row < len(self.grid) - 1:
            if self.grid[row+1][col] == color:
                code = str(row+1) + "_" + str(col)
                if code not in self.component:
                    self.formComponent(row+1, col, color)
        if col > 0:
            if self.grid[row][col-1] == color:
                code = str(row) + "_" + str(col-1)
                if code not in self.component:
                    self.formComponent(row, col-1, color)
        if col < len(self.grid[0]) - 1:
            if self.grid[row][col+1] == color:
                code = str(row) + "_" + str(col+1)
                if code not in self.component:
                    self.formComponent(row, col+1, color)

    def findBorder(self, color):
        res = []
        for code in self.component:
            row, col = code.split("_")
            row = int(row)
            col = int(col)
            if (row > 0) and (col > 0) and (row < len(self.grid) - 1) and (col < len(self.grid[0]) - 1):
                if (self.grid[row-1][col] == color) and (self.grid[row+1][col] == color) and (self.grid[row][col-1] == color) and (self.grid[row][col+1] == color):
                    continue
                else:
                    res.append([row, col])
            else:
                res.append([row, col])
        return res
