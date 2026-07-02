# You are given an m x n integer matrix mat and an integer target.
# Choose one integer from each row in the matrix such that the absolute difference between target and the sum of the chosen elements is minimized.
# Return the minimum absolute difference.
# The absolute difference between two numbers a and b is the absolute value of a - b.
from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        sums_set = set([0])
        for i in range(len(mat)):
            cur_sums = set()
            for j in range(len(mat[0])):
                cur_sums.add(mat[i][j])
            new_sums = set()
            for sum1 in sums_set:
                for sum2 in cur_sums:
                    new_sums.add(sum1 + sum2)
            sums_set = new_sums
        return min([abs(elem - target) for elem in sums_set])
