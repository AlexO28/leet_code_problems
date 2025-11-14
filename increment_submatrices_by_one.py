# You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.
# You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:
# Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.
# Return the matrix mat after performing every query.
from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        S = [[0] * n for i in range(n)]
        for row1, col1, row2, col2 in queries:
            for j in range(row1, row2 + 1):
                S[j][col1] += 1
                if col2 < n - 1:
                    S[j][col2 + 1] -= 1
        for i in range(n):
            for j in range(1, n):
                S[i][j] += S[i][j - 1]
        return S
