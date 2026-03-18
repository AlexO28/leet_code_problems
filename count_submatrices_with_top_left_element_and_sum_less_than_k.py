# You are given a 0-indexed integer matrix grid and an integer k.
# Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.
from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        s = [[0] * (len(grid[0]) + 1) for i in range(len(grid) + 1)]
        ans = 0
        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + x
                ans += s[i][j] <= k
        return ans
