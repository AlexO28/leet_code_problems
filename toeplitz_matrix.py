# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if (len(matrix) == 1) or (len(matrix[0]) == 1):
            return True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
