# You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).
# Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.
# The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
from typing import List
from collections import deque


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        queue = deque([[rCenter, cCenter]])
        visited = [[False] * cols for i in range(rows)]
        visited[rCenter][cCenter] = True
        result = []
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            current_cell = queue.popleft()
            result.append(current_cell)          
            for delta_row, delta_col in directions:
                new_row = current_cell[0] + delta_row
                new_col = current_cell[1] + delta_col
                if (new_row >= 0) and (new_row < rows) and (new_col >= 0) and (new_col < cols):
                    if not visited[new_row][new_col]:
                        visited[new_row][new_col] = True
                        queue.append([new_row, new_col])
        return result
