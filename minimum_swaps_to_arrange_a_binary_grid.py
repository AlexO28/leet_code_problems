# Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
# A grid is said to be valid if all the cells above the main diagonal are zeros.
# Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        rightmost_one_positions = [-1] * (len(grid))
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid) - 1, -1, -1):
                if grid[row_idx][col_idx] == 1:
                    rightmost_one_positions[row_idx] = col_idx
                    break
        total_swaps = 0
        for target_row in range(len(grid)):
            suitable_row_idx = -1
            for candidate_row in range(target_row, len(grid)):
                if rightmost_one_positions[candidate_row] <= target_row:
                    total_swaps += candidate_row - target_row
                    suitable_row_idx = candidate_row
                    break
            if suitable_row_idx == -1:
                return -1
            while suitable_row_idx > target_row:
                (
                    rightmost_one_positions[suitable_row_idx],
                    rightmost_one_positions[suitable_row_idx - 1],
                ) = (
                    rightmost_one_positions[suitable_row_idx - 1],
                    rightmost_one_positions[suitable_row_idx],
                )
                suitable_row_idx -= 1
        return total_swaps
