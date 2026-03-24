# Given a 0-indexed 2D integer matrix grid of size n * m, we define a 0-indexed 2D matrix p of size n * m as the product matrix of grid if the following condition is met:
# Each element p[i][j] is calculated as the product of all elements in grid except for the element grid[i][j]. This product is then taken modulo 12345.
# Return the product matrix of grid.
from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        p = [[0] * len(grid[0]) for i in range(len(grid))]
        MOD = 12345
        suf = 1
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                p[i][j] = suf
                suf = suf * grid[i][j] % MOD
        pre = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                p[i][j] = p[i][j] * pre % MOD
                pre = pre * grid[i][j] % MOD
        return p
