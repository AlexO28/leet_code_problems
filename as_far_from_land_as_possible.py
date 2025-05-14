# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.
# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        land_cells = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land_cells.append([i, j])
        max_len = len(grid) * len(grid[0])
        if (len(land_cells) == max_len) or (len(land_cells) == 0):
            return -1
        number_of_trials = 0
        boundary_land_cells = land_cells.copy()
        while len(land_cells) < max_len:
            new_land_cells = []
            number_of_trials += 1
            for i, j in boundary_land_cells:
                if (i > 0) and (grid[i-1][j] == 0):
                    new_land_cells.append([i-1, j])
                    grid[i-1][j] = 1
                    land_cells.append([i-1, j])
                if (j > 0) and (grid[i][j-1] == 0):
                    new_land_cells.append([i, j-1])
                    grid[i][j-1] = 1
                    land_cells.append([i, j-1])
                if (i < len(grid) - 1) and (grid[i+1][j] == 0):
                    new_land_cells.append([i+1, j])
                    grid[i+1][j] = 1
                    land_cells.append([i+1, j])
                if (j < len(grid[0]) - 1) and (grid[i][j+1] == 0):
                    new_land_cells.append([i, j+1])
                    grid[i][j+1] = 1
                    land_cells.append([i, j+1])
            boundary_land_cells = new_land_cells.copy()
        return number_of_trials
