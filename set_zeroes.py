# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_indices = []
        col_indices = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in row_indices:
                        row_indices.append(i)
                    if j not in col_indices:
                        col_indices.append(j)
        if len(row_indices) > 0: 
            for i in row_indices:
                for j in range(n):
                    matrix[i][j] = 0
        if len(col_indices) > 0:
            for j in col_indices:
                for i in range(m):
                    matrix[i][j] = 0
