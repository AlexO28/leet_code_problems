# In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1). The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).
# In one move the snake can:
# Move one cell to the right if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
# Move down one cell if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
# Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).
# Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty. In that case the snake moves from (r, c) and (r+1, c) to (r, c) and (r, c+1).
# Return the minimum number of moves to reach the target.
# If there is no way to reach the target, return -1.
from typing import List
from collections import deque


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        self.grid = [grid[i].copy() for i in range(len(grid))]
        grid_sqr = len(grid) ** 2
        target = (grid_sqr - 2, grid_sqr - 1)
        self.queue = deque([(0, 1)])
        self.visited = {(0, 0)}
        moves_count = 0

        while self.queue:
            for i in range(len(self.queue)):
                start_pos, end_pos = self.queue.popleft()
                if (start_pos, end_pos) == target:
                    return moves_count
                start_row, start_col = divmod(start_pos, len(grid))
                end_row, end_col = divmod(end_pos, len(grid))
                self.move(start_row, start_col + 1, end_row, end_col + 1)
                self.move(start_row + 1, start_col, end_row + 1, end_col)
                if (
                    start_row == end_row
                    and start_row + 1 < len(grid)
                    and grid[start_row + 1][end_col] == 0
                ):
                    self.move(start_row, start_col, start_row + 1, start_col)
                if (
                    start_col == end_col
                    and start_col + 1 < len(grid)
                    and grid[end_row][start_col + 1] == 0
                ):
                    self.move(start_row, start_col, start_row, start_col + 1)
            moves_count += 1
        return -1

    def move(self, start_row, start_col, end_row, end_col):
        if (
            0 <= start_row < len(self.grid)
            and 0 <= start_col < len(self.grid)
            and 0 <= end_row < len(self.grid)
            and 0 <= end_col < len(self.grid)
        ):
            start_pos = start_row * len(self.grid) + start_col
            end_pos = end_row * len(self.grid) + end_col
            if start_row == end_row:
                status = 0
            else:
                status = 1
            if (
                (start_pos, status) not in self.visited
                and self.grid[start_row][start_col] == 0
                and self.grid[end_row][end_col] == 0
            ):
                self.queue.append((start_pos, end_pos))
                self.visited.add((start_pos, status))
