# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
# A land cell if grid[r][c] = 0, or
# A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations any number of times:
# Catch all the fish at cell (r, c), or
# Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.
# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_fish = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    max_fish = max(max_fish, self.catchAllFish(grid, i, j))
        return max_fish

    def catchAllFish(self, grid, x, y):
        cur_fish = 0
        if grid[x][y] > 0:
            cur_fish += grid[x][y]
            grid[x][y] = -1
        if x > 0:
            if grid[x-1][y] > 0:
                cur_fish += self.catchAllFish(grid, x-1, y)
        if x < len(grid)-1:
            if grid[x+1][y] > 0:
                cur_fish += self.catchAllFish(grid, x+1, y)
        if y > 0:
            if grid[x][y-1] > 0:
                cur_fish += self.catchAllFish(grid, x, y-1)
        if y < len(grid[0])-1:
            if grid[x][y+1] > 0:
                cur_fish += self.catchAllFish(grid, x, y+1)
        return cur_fish
