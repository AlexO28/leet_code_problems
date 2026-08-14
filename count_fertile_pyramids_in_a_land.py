# A farmer has a rectangular grid of land with m rows and n columns that can be divided into unit cells. Each cell is either fertile (represented by a 1) or barren (represented by a 0). All cells outside the grid are considered barren.
# A pyramidal plot of land can be defined as a set of cells with the following criteria:
# The number of cells in the set has to be greater than 1 and all cells must be fertile.
# The apex of a pyramid is the topmost cell of the pyramid. The height of a pyramid is the number of rows it covers. Let (r, c) be the apex of the pyramid, and its height be h. Then, the plot comprises of cells (i, j) where r <= i <= r + h - 1 and c - (i - r) <= j <= c + (i - r).
# An inverse pyramidal plot of land can be defined as a set of cells with similar criteria:
# The number of cells in the set has to be greater than 1 and all cells must be fertile.
# The apex of an inverse pyramid is the bottommost cell of the inverse pyramid. The height of an inverse pyramid is the number of rows it covers. Let (r, c) be the apex of the pyramid, and its height be h. Then, the plot comprises of cells (i, j) where r - h + 1 <= i <= r and c - (r - i) <= j <= c + (r - i).
# Some examples of valid and invalid pyramidal (and inverse pyramidal) plots are shown below. Black cells indicate fertile cells.
from typing import List


class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        f = [[0] * len(grid[0]) for _ in range(len(grid))]
        ans = 0
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    f[i][j] = -1
                elif not ((i == len(grid) - 1) or (j == 0) or (j == len(grid[0]) - 1)):
                    f[i][j] = min(f[i + 1][j - 1], f[i + 1][j], f[i + 1][j + 1]) + 1
                    ans += f[i][j]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    f[i][j] = -1
                elif (i == 0) or (j == 0) or (j == len(grid[0]) - 1):
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i - 1][j + 1]) + 1
                    ans += f[i][j]
        return ans
