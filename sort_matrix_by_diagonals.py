# You are given an n x n square matrix of integers grid. Return the matrix such that:
# The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
# The diagonals in the top-right triangle are sorted in non-decreasing order.
from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        if len(grid) > 1:
            for margin in range(0, len(grid) - 1):
                temp_arr = []
                for i in range(len(grid)):
                    if i + margin < len(grid):
                        temp_arr.append(grid[i + margin][i])
                    else:
                        break
                temp_arr.sort(reverse=True)
                for i in range(len(grid)):
                    if i + margin < len(grid):
                        grid[i + margin][i] = temp_arr[i]
                    else:
                        break
            if len(grid) > 2:
                for margin in range(1, len(grid) - 1):
                    temp_arr = []
                    for i in range(len(grid)):
                        if i + margin < len(grid):
                            temp_arr.append(grid[i][i + margin])
                        else:
                            break
                    temp_arr.sort()
                    for i in range(len(grid)):
                        if i + margin < len(grid):
                            grid[i][i + margin] = temp_arr[i]
                        else:
                            break
        return grid
