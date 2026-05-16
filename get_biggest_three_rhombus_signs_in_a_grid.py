# You are given an m x n integer matrix grid​​​.
# A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:
# Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.
# Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.
from sortedcontainers import SortedSet
from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        s1 = [[0] * (len(grid[0]) + 2) for _ in range(len(grid) + 1)]
        s2 = [[0] * (len(grid[0]) + 2) for _ in range(len(grid) + 1)]
        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                s1[i][j] = s1[i - 1][j - 1] + x
                s2[i][j] = s2[i - 1][j + 1] + x
        ss = SortedSet()
        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                l = min(i - 1, len(grid) - i, j - 1, len(grid[0]) - j)
                ss.add(x)
                for k in range(1, l + 1):
                    a = s1[i + k][j] - s1[i][j - k]
                    b = s1[i][j + k] - s1[i - k][j]
                    c = s2[i][j - k] - s2[i - k][j]
                    d = s2[i + k][j] - s2[i][j + k]
                    ss.add(
                        a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]
                    )
                while len(ss) > 3:
                    ss.remove(ss[0])
        return list(ss)[::-1]
