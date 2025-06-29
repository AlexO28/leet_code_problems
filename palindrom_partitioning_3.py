# You are given a string s containing lowercase letters and an integer k. You need to :
# First, change some characters of s to other lowercase English letters.
# Then divide s into k non-empty disjoint substrings such that each substring is a palindrome.
# Return the minimal number of characters that you need to change to divide the string.
from math import inf


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        changes = [[0] * len(s) for i in range(len(s))]
        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 1, len(s)):
                changes[start][end] = int(s[start] != s[end])
                if start + 1 < end:
                    changes[start][end] += changes[start + 1][end - 1]
        dp = [[inf] * (k + 1) for i in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, min(i, k) + 1):
                if j == 1:
                    dp[i][j] = changes[0][i - 1]
                else:
                    for h in range(j - 1, i):
                        dp[i][j] = min(dp[i][j], dp[h][j - 1] + changes[h][i - 1])
        return dp[len(s)][k]
