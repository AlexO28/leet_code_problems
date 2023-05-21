# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


import numpy as np


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n > 1:
            for j in range(int(np.floor(n/2))):
                for k in range(int(np.ceil(n/2))):
                    matrix[k][j], matrix[j][n-k-1], matrix[n-k-1][n-j-1], matrix[n-j-1][k] = matrix[n-j-1][k], matrix[k][j], matrix[j][n-k-1], matrix[n-k-1][n-j-1]
