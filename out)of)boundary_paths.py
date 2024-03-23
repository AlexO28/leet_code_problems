# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
from functools import cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        self.m = m
        self.n = n
        self.MOD = 10**9 + 7
        return self.search(startRow, startColumn, maxMove)

    @cache
    def search(self, row, col, maxMove):
        if row < 0 or col < 0 or row >= self.m or col >= self.n:
            return 1
        if maxMove <= 0:
            return 0
        paths_count = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for direction in directions:
            new_row, new_col = row + direction[0], col + direction[1]
            paths_count += self.search(new_row, new_col, maxMove - 1)
            paths_count %= self.MOD
        return paths_count
