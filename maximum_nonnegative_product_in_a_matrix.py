# You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.
# Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.
# Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.
# Notice that the modulo is performed after getting the maximum product.
from typing import List
from functools import cache


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        self.grid = grid
        best = self.calculate(str(0) + ":" + str(0))[0]
        if best < 0:
            return -1
        else:
            return best % 1000000007

    @cache
    def calculate(self, coordinates):
        start, end = coordinates.split(":")
        start = int(start)
        end = int(end)
        if (start == len(self.grid) - 1) and (end == len(self.grid[0]) - 1):
            return self.grid[start][end], self.grid[start][end]
        elif start == len(self.grid) - 1:
            if self.grid[start][end] == 0:
                return 0, 0
            elif self.grid[start][end] > 0:
                best, worst = self.calculate(str(start) + ":" + str(end + 1))
                return (
                    self.grid[start][end] * best,
                    self.grid[start][end] * worst,
                )
            else:
                best, worst = self.calculate(str(start) + ":" + str(end + 1))[::-1]
                return (
                    self.grid[start][end] * worst,
                    self.grid[start][end] * best,
                )
        elif end == len(self.grid[0]) - 1:
            if self.grid[start][end] == 0:
                return 0, 0
            elif self.grid[start][end] > 0:
                best, worst = self.calculate(str(start + 1) + ":" + str(end))
                return (
                    self.grid[start][end] * best,
                    self.grid[start][end] * worst,
                )
            else:
                best, worst = self.calculate(str(start + 1) + ":" + str(end))
                return (
                    self.grid[start][end] * worst,
                    self.grid[start][end] * best,
                )
        else:
            if self.grid[start][end] == 0:
                return 0, 0
            else:
                best1, worst1 = self.calculate(str(start + 1) + ":" + str(end))
                best2, worst2 = self.calculate(str(start) + ":" + str(end + 1))
                results = [best1, worst1, best2, worst2]
                results.sort()
                if self.grid[start][end] > 0:
                    return (
                        self.grid[start][end] * results[-1],
                        self.grid[start][end] * results[0],
                    )
                else:
                    return (
                        self.grid[start][end] * results[0],
                        self.grid[start][end] * results[-1],
                    )
