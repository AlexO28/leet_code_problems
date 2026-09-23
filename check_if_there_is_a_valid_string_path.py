# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
# It is ().
# It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# It can be written as (A), where A is a valid parentheses string.
# You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:
# The path starts from the upper left cell (0, 0).
# The path ends at the bottom-right cell (m - 1, n - 1).
# The path only ever moves down or right.
# The resulting parentheses string formed by the path is valid.
# Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.
from functools import cache
from itertools import pairwise


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        self.grid = grid
        if (
            (len(grid) + len(grid[0]) - 1) % 2
            or grid[0][0] == ")"
            or grid[-1][-1] == "("
        ):
            return False
        else:
            return self.search(0, 0, 0)

    @cache
    def search(self, i, j, k):
        if self.grid[i][j] == "(":
            d = 1
        else:
            d = -1
        k += d
        if k < 0 or k > len(self.grid) - i + len(self.grid[0]) - j:
            return False
        if i == len(self.grid) - 1 and j == len(self.grid[0]) - 1:
            return k == 0
        for a, b in pairwise((0, 1, 0)):
            x = i + a
            y = j + b
            if (
                0 <= x < len(self.grid)
                and 0 <= y < len(self.grid[0])
                and self.search(x, y, k)
            ):
                return True
        return False
