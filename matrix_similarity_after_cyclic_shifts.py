# You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.
# The following proccess happens k times:
# Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
# Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.
# Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.
from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k = k % len(mat[0])
        if k == 0:
            return True
        for i in range(len(mat)):
            if i % 2 == 0:
                next_line = mat[i][k:] + mat[i][:k]
            else:
                next_line = mat[i][(-k):] + mat[i][:(-k)]
            if next_line != mat[i]:
                return False
        return True
