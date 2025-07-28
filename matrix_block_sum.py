# Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:
# i - k <= r <= i + k,
# j - k <= c <= j + k, and
# (r, c) is a valid position in the matrix.
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        arr = [[0] * (len(mat[0]) + 1) for i in range(len(mat))]
        for i in range(len(arr)):
            cursum = 0
            arr[i][0] = cursum
            for j in range(1, len(arr[0])):
                cursum += mat[i][j - 1]
                arr[i][j] = cursum
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                summa = 0
                for z in range(max(i - k, 0), min(i + k + 1, len(mat))):
                    summa += arr[z][min(j + k + 1, len(mat[0]))] - arr[z][max(j - k, 0)]
                mat[i][j] = summa
        return mat
