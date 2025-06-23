# A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.
# The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.
# Your task is to move the box 'B' to the target position 'T' under the following rules:
# The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
# The character '.' represents the floor which means a free cell to walk.
# The character '#' represents the wall which means an obstacle (impossible to walk there).
# There is only one box 'B' and one target cell 'T' in the grid.
# The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
# The player cannot walk through the box.
# Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.
from typing import List
from collections import deque


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        self.grid = grid
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == "S":
                    start_row, start_col = i, j
                elif cell == "B":
                    box_row, box_col = i, j
        directions = (-1, 0, 1, 0, -1)
        queue = deque(
            [
                (
                    self.get_flat_index(start_row, start_col),
                    self.get_flat_index(box_row, box_col),
                    0,
                )
            ]
        )
        prod = len(self.grid) * len(self.grid[0])
        visited = [[False] * prod for _ in range(prod)]
        visited[self.get_flat_index(start_row, start_col)][
            self.get_flat_index(box_row, box_col)
        ] = True
        while queue:
            player, box, distance = queue.popleft()
            box_row, box_col = divmod(box, len(self.grid[0]))
            if self.grid[box_row][box_col] == "T":
                return distance
            player_row, player_col = divmod(player, len(self.grid[0]))
            for delta_row, delta_col in zip(directions, directions[1:]):
                next_player_row, next_player_col = (
                    player_row + delta_row,
                    player_col + delta_col,
                )
                if not self.is_valid(next_player_row, next_player_col):
                    continue
                index_next_player = self.get_flat_index(
                    next_player_row, next_player_col
                )
                index_box = self.get_flat_index(box_row, box_col)
                if next_player_row == box_row and next_player_col == box_col:
                    next_box_row, next_box_col = (
                        box_row + delta_row,
                        box_col + delta_col,
                    )
                    index_next_box = self.get_flat_index(next_box_row, next_box_col)
                    if (
                        not self.is_valid(next_box_row, next_box_col)
                        or visited[index_next_player][index_next_box]
                    ):
                        continue
                    visited[index_next_player][index_next_box] = True
                    queue.append(
                        (
                            index_next_player,
                            index_next_box,
                            distance + 1,
                        )
                    )
                elif not visited[index_next_player][index_box]:
                    visited[self.get_flat_index(next_player_row, next_player_col)][
                        index_box
                    ] = True
                    queue.appendleft(
                        (
                            index_next_player,
                            index_box,
                            distance,
                        )
                    )
        return -1

    def get_flat_index(self, row, col):
        return row * len(self.grid[0]) + col

    def is_valid(self, row, col):
        return (
            0 <= row < len(self.grid)
            and 0 <= col < len(self.grid[0])
            and self.grid[row][col] != "#"
        )
