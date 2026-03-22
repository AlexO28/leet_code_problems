# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if self.areEqual(mat, target):
            return True
        for i in range(3):
            mat = self.rotate(mat)
            if self.areEqual(mat, target):
                return True
        return False

    def areEqual(self, mat1, mat2):
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                if mat1[i][j] != mat2[i][j]:
                    return False
        return True

    def rotate(self, mat):
        new_mat = [[0] * len(mat[0]) for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                new_mat[j][len(mat) - i - 1] = mat[i][j]
        return new_mat
