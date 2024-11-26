# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
from functools import cache


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        min_sum = 100000
        for j in range(len(self.matrix)):
            min_sum = min(min_sum, self.calculate_falling_sum(0, j))
        return min_sum

    @cache
    def calculate_falling_sum(self, i, j):
        if i == len(self.matrix)-1:
            return self.matrix[i][j]
        else:
            res = self.matrix[i][j]
            candidates = []
            candidates.append(self.calculate_falling_sum(i+1, j))
            if j > 0:
                candidates.append(self.calculate_falling_sum(i+1, j-1))
            if j < len(self.matrix)-1:
                candidates.append(self.calculate_falling_sum(i+1, j+1))
            return res + min(candidates)
