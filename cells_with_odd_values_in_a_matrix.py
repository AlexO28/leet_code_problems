# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.
# For each location indices[i], do both of the following:
# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0] * n for i in range(m)]
        for x, y in indices:
            for z in range(n):
                mat[x][z] += 1
            for z in range(m):
                mat[z][y] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] % 2 > 0:
                    res += 1
        return res
