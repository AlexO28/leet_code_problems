# You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.
# You have two robots that can collect cherries for you:
# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of cherries collection using both robots by following the rules below:
# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid.
from typing import List
from itertools import product


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = [
            [[-1] * (len(grid[0])) for i in range(len(grid[0]))]
            for j in range(len(grid))
        ]
        dp[0][0][len(grid[0]) - 1] = grid[0][0] + grid[0][-1]
        for row in range(1, len(grid)):
            for col1 in range(len(grid[0])):
                for col2 in range(len(grid[0])):
                    if col1 == col2:
                        current_cherries = grid[row][col1]
                    else:
                        current_cherries = grid[row][col1] + grid[row][col2]
                    for prev_col1 in range(col1 - 1, col1 + 2):
                        for prev_col2 in range(col2 - 1, col2 + 2):
                            if (
                                (0 <= prev_col1 < len(grid[0]))
                                and (0 <= prev_col2 < len(grid[0]))
                                and (dp[row - 1][prev_col1][prev_col2] != -1)
                            ):
                                dp[row][col1][col2] = max(
                                    dp[row][col1][col2],
                                    dp[row - 1][prev_col1][prev_col2]
                                    + current_cherries,
                                )
        return max(
            dp[-1][col1][col2]
            for col1, col2 in product(range(len(grid[0])), range(len(grid[0])))
            if dp[-1][col1][col2] != -1
        )
