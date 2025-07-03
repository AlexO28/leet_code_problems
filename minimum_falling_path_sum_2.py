# Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.
# A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.
from math import inf
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        smallest_fall = 0
        second_smallest_fall = 0
        smallest_fall_position = -1
        for row in grid:
            current_smallest = inf
            current_second_smallest = inf
            current_smallest_position = -1
            for j, value in enumerate(row):
                total_path_sum = (
                    second_smallest_fall
                    if j == smallest_fall_position
                    else smallest_fall
                ) + value
                if total_path_sum < current_smallest:
                    current_second_smallest = current_smallest
                    current_smallest = total_path_sum
                    current_smallest_position = j
                elif total_path_sum < current_second_smallest:
                    current_second_smallest = total_path_sum
            smallest_fall = current_smallest
            second_smallest_fall = current_second_smallest
            smallest_fall_position = current_smallest_position
        return smallest_fall
 
