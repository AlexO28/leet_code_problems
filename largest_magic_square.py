# A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.
# Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.
from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        if (len(grid) == 1) or (len(grid[0]) == 1):
            return 1
        self.rowsum = [[0] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        self.colsum = [[0] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                self.rowsum[i][j] = self.rowsum[i][j - 1] + grid[i - 1][j - 1]
                self.colsum[i][j] = self.colsum[i - 1][j] + grid[i - 1][j - 1]
        for k in range(min(len(grid), len(grid[0])), 1, -1):
            i = 0
            while i + k - 1 < len(grid):
                j = 0
                while j + k - 1 < len(grid[0]):
                    i2 = i + k - 1
                    j2 = j + k - 1
                    if self.check(grid, i, j, i2, j2):
                        return k
                    j += 1
                i += 1
        return 1

    def check(self, grid, x1, y1, x2, y2):
        val = self.rowsum[x1 + 1][y2 + 1] - self.rowsum[x1 + 1][y1]
        for i in range(x1 + 1, x2 + 1):
            if self.rowsum[i + 1][y2 + 1] - self.rowsum[i + 1][y1] != val:
                return False
        for j in range(y1, y2 + 1):
            if self.colsum[x2 + 1][j + 1] - self.colsum[x1][j + 1] != val:
                return False
        s = 0
        i = x1
        j = y1
        while i <= x2:
            s += grid[i][j]
            i += 1
            j += 1
        if s != val:
            return False
        s = 0
        i = x1
        j = y2
        while i <= x2:
            s += grid[i][j]
            i += 1
            j -= 1
        if s != val:
            return False
        return True
