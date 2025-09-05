# Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
# 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some signs on the cells of the grid that point outside the grid.
# You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.
# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.
# Return the minimum cost to make the grid have at least one valid path.
from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque([(0, 0, 0)])
        visited = set()
        while queue:
            current_row, current_col, current_cost = queue.popleft()
            if (current_row, current_col) in visited:
                continue
            visited.add((current_row, current_col))
            if current_row == len(grid) - 1 and current_col == len(grid[0]) - 1:
                return current_cost
            for direction_index in range(1, 5):
                next_row = current_row + directions[direction_index][0]
                next_col = current_col + directions[direction_index][1]
                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                    if grid[current_row][current_col] == direction_index:
                        queue.appendleft((next_row, next_col, current_cost))
                    else:
                        queue.append((next_row, next_col, current_cost + 1))
        return -1
