# You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.
# Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).
# At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.
# The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.
from typing import List
from math import inf


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        if len(grid[0]) == 1:
            return 0
        sums_1 = []
        sums_2 = []
        cur_sum = 0
        for j in range(len(grid[0])):
            cur_sum += grid[0][j]
            sums_1.append(cur_sum)
        cur_sum = 0
        for j in range(len(grid[0])):
            cur_sum += grid[1][j]
            sums_2.append(cur_sum)
        min_sum = inf
        for j in range(len(grid[0])):
            if j > 0:
                sum_second = max(sums_2[j - 1], sums_1[-1] - sums_1[j])
            else:
                sum_second = sums_1[-1] - sums_1[0]
            min_sum = min(min_sum, sum_second)
        return min_sum
