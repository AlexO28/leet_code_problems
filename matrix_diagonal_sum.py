# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        main_part, remainder = divmod(len(mat), 2)
        if remainder == 1:
            summa = -mat[main_part][main_part]
        else:
            summa = 0
        for i in range(len(mat)):
            summa += mat[i][i] + mat[len(mat)-i-1][i]
        return summa
