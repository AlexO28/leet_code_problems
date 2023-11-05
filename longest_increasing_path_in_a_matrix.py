# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        @lru_cache(maxsize=None)
        def dfs(y, x):
            val = matrix[y][x]
            max_val = 0
            if y < len(matrix) - 1:
                if val > matrix[y+1][x]:
                    max_val = max(dfs(y+1, x), max_val)
            if y > 0:
                if val > matrix[y-1][x]:
                    max_val = max(dfs(y-1, x), max_val)
            if x < len(matrix[0]) - 1:
                if val > matrix[y][x+1]:
                    max_val = max(dfs(y, x+1), max_val)
            if x > 0:
                if val > matrix[y][x-1]:
                    max_val = max(dfs(y, x-1), max_val)
            return 1 + max_val

        max_val = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                max_val = max(max_val, dfs(y, x))
        return max_val
