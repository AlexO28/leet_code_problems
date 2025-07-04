# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.
from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        self.mat = mat
        self.prefix_sum = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                self.prefix_sum[i][j] = (
                    self.prefix_sum[i - 1][j]
                    + self.prefix_sum[i][j - 1]
                    - self.prefix_sum[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )
        left = 0
        right = min(len(mat), len(mat[0]))
        while left < right:
            mid = (left + right + 1) // 2
            if self.check_square_fits(mid, threshold):
                left = mid
            else:
                right = mid - 1
        return left

    def check_square_fits(self, k, threshold):
        for i in range(len(self.mat) - k + 1):
            for j in range(len(self.mat[0]) - k + 1):
                square_sum = (
                    self.prefix_sum[i + k][j + k]
                    - self.prefix_sum[i][j + k]
                    - self.prefix_sum[i + k][j]
                    + self.prefix_sum[i][j]
                )
                if square_sum <= threshold:
                    return True
        return False
