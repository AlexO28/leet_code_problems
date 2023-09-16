# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) 
                    max_area = max(max_area, dp[i + 1][j + 1])
        return max_area ** 2
