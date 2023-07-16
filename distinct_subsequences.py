# Given two strings s and t, return the number of distinct subsequences of s which equals t.
import numpy as np


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = np.zeros(shape = [len(s)+1, len(t)+1])
        dp[0][0] = 1
        for i in range(1, len(s)+1):
            dp[i][0] = 1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if (i > 0) and (j > 0):
                    if s[len(s)-i] == t[len(t)-j]:
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                    else:
                        dp[i][j] = dp[i-1][j]
        return int(dp[len(s)][len(t)])
