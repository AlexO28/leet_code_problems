# You are given a 2D integer array grid of size m x n, where each cell contains a positive integer.
# A cornered path is defined as a set of adjacent cells with at most one turn. More specifically, the path should exclusively move either horizontally or vertically up to the turn (if there is one), without returning to a previously visited cell. After the turn, the path will then move exclusively in the alternate direction: move vertically if it moved horizontally, and vice versa, also without returning to a previously visited cell.
# The product of a path is defined as the product of all the values in the path.
# Return the maximum number of trailing zeros in the product of a cornered path found in grid.
# Note:
# Horizontal movement means moving in either the left or right direction.
# Vertical movement means moving in either the up or down direction.
from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m = len(grid) + 1
        n = len(grid[0]) + 1
        r2 = [[0] * n for _ in range(m)]
        c2 = [[0] * n for _ in range(m)]
        r5 = [[0] * n for _ in range(m)]
        c5 = [[0] * n for _ in range(m)]
        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                s2 = 0
                s5 = 0
                remainder = 0
                while x > 0:
                    main_part, remainder = divmod(x, 2)
                    if remainder > 0:
                        break
                    s2 += 1
                    x = main_part
                remainder = 0
                while x > 0:
                    main_part, remainder = divmod(x, 5)
                    if remainder > 0:
                        break
                    s5 += 1
                    x = main_part
                r2[i][j] = r2[i][j - 1] + s2
                c2[i][j] = c2[i - 1][j] + s2
                r5[i][j] = r5[i][j - 1] + s5
                c5[i][j] = c5[i - 1][j] + s5
        ans = 0
        for i in range(1, m):
            for j in range(1, n):
                a = min(r2[i][j] + c2[i - 1][j], r5[i][j] + c5[i - 1][j])
                b = min(
                    r2[i][j] + c2[-1][j] - c2[i][j], r5[i][j] + c5[-1][j] - c5[i][j]
                )
                c = min(
                    r2[i][-1] - r2[i][j] + c2[i][j], r5[i][-1] - r5[i][j] + c5[i][j]
                )
                d = min(
                    r2[i][-1] - r2[i][j - 1] + c2[-1][j] - c2[i][j],
                    r5[i][-1] - r5[i][j - 1] + c5[-1][j] - c5[i][j],
                )
                ans = max(ans, a, b, c, d)
        return ans
