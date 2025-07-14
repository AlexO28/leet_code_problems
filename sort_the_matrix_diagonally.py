# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(mat[0]) for i in range(len(mat))]
        for diag_id in range(-len(mat[0]) + 1, len(mat)):
            temp = []
            for i in range(len(mat)):
                j = i - diag_id
                if (j >= 0) and (j < len(mat[0])):
                    temp.append(mat[i][j])
            temp.sort()
            counter = 0
            for i in range(len(mat)):
                j = i - diag_id
                if (j >= 0) and (j < len(mat[0])):
                    res[i][j] = temp[counter]
                    counter += 1
        return res
