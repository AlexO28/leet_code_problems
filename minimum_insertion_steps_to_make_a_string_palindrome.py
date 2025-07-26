# Given a string s. In one step you can insert any character at any index of the string.
# Return the minimum number of steps to make s palindrome.
# A Palindrome String is one that reads the same backward as well as forward.
class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[0] * len(s) for i in range(len(s))]
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][-1]
