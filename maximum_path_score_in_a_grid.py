# You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.
# You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.
# Each cell contributes a specific score and incurs an associated cost, according to their cell values:
# 0: adds 0 to your score and costs 0.
# 1: adds 1 to your score and costs 1.
# 2: adds 2 to your score and costs 1. ​​​​​​​
# Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.
# Note: If you reach the last cell but the total cost exceeds k, the path is invalid.
from typing import List
from functools import cache
from math import inf


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        self.grid = grid
        ans = self.search(len(grid) - 1, len(grid[0]) - 1, k)
        self.search.cache_clear()
        if ans < 0:
            return -1
        else:
            return ans

    @cache
    def search(self, i, j, k):
        if (i < 0) or (j < 0) or (k < 0):
            return -inf
        if (i == 0) and (j == 0):
            return 0
        res = self.grid[i][j]
        if self.grid[i][j]:
            k -= 1
        return self.grid[i][j] + max(self.search(i - 1, j, k), self.search(i, j - 1, k))
