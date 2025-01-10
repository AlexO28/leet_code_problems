# You are given an m x n integer array grid where grid[i][j] could be:
# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_x, start_y = next((i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1)
        self.directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        self.empty_squares = 1 + sum(row.count(0) for row in grid)
        self.visited = {(start_x, start_y)}
        return self.search(start_x, start_y, 0, grid)

    def search(self, x, y, steps, grid):
        if grid[x][y] == 2:
            return int(steps == self.empty_squares)
        else:
            path_count = 0
            for dx, dy in self.directions:
                next_x = x + dx
                next_y = y + dy
                if (next_x >= 0) and (next_x < len(grid)) and (next_y >= 0) and (next_y < len(grid[0])) and ((next_x, next_y) not in self.visited) and (grid[next_x][next_y] != -1):
                    self.visited.add((next_x, next_y))
                    path_count += self.search(next_x, next_y, steps + 1, grid)
                    self.visited.remove((next_x, next_y))
            return path_count
