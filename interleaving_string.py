# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

import numpy as np


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s3) == 0:
            return (len(s1) == 0) and (len(s2) == 0)
        if len(s1) == 0:
            return s3 == s2
        if len(s3) == 0:
            return s3 == s1
        dp = np.zeros([len(s1)+1, len(s2)+1])
        dp[0, 0] = True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if (i == 0) and (j == 0):
                    continue
                check1 = False
                check2 = False
                if i > 0:
                    if s1[i - 1] == s3[i + j - 1]:
                        check1 = dp[i-1, j]
                if j > 0:
                    if s2[j - 1] == s3[i + j - 1]:
                        check2 = dp[i, j-1]
                dp[i, j] = check1 or check2
        return dp[len(s1), len(s2)]
