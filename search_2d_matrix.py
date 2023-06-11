# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat_vec = []
        for i in range(len(matrix)):
            mat_vec.extend(matrix[i])
        return target in mat_vec
