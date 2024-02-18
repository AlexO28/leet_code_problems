# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 1:
            return 1
        dp = [[0] * len(s) for j in range(len(s))]
        for j in range(len(s)):
            dp[j][j] = 1
        for j in range(1, len(s)):
            for i in range(j-1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])                  
        return dp[0][len(s) - 1]
