# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
# Return the smallest index i at which either a row or a column will be completely painted in mat.
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num_dict = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                num_dict[mat[i][j]] = [i, j]
        row_freqs = [0]*len(mat)
        col_freqs = [0]*len(mat[0])
        for k in range(len(arr)):
            i, j = num_dict[arr[k]]
            row_freqs[i] += 1
            if row_freqs[i] == len(mat[0]):
                return k
            col_freqs[j] += 1
            if col_freqs[j] == len(mat):
                return k
