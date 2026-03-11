# You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.
# The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).
# Find the kth largest value (1-indexed) of all the coordinates of matrix.
from typing import List
from heapq import nlargest


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        s = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s[i + 1][j + 1] = s[i + 1][j] ^ s[i][j + 1] ^ s[i][j] ^ matrix[i][j]
                ans.append(s[i + 1][j + 1])
        return nlargest(k, ans)[-1]
