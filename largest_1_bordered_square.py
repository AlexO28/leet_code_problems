# Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        down = [[0] * (len(grid[0])) for i in range(len(grid))]
        right = [[0] * (len(grid[0])) for i in range(len(grid))]
        for row in range(len(grid) - 1, -1, -1):
            for col in range(len(grid[0]) - 1, -1, -1):
                if grid[row][col] == 1:
                    if row + 1 < len(grid):
                        down[row][col] = 1 + down[row + 1][col] 
                    else:
                        down[row][col] = 1
                    if col + 1 < len(grid[0]):
                        right[row][col] = 1 + right[row][col + 1]
                    else:
                        right[row][col] = 1
        for max_side in range(min(len(grid), len(grid[0])), 0, -1):
            for row in range(len(grid) - max_side + 1):
                for col in range(len(grid[0]) - max_side + 1):
                    if (down[row][col] >= max_side) and (right[row][col] >= max_side) and (right[row + max_side - 1][col] >= max_side) and (down[row][col + max_side - 1] >= max_side):
                        return max_side * max_side
        return 0
