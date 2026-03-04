# You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.
# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.
from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    matrix[i][j] = matrix[i - 1][j] + 1
        ans = 0
        for row in matrix:
            row.sort(reverse=True)
            for j, v in enumerate(row, 1):
                ans = max(ans, j * v)
        return ans
