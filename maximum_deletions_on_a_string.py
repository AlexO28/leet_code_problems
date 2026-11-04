# You are given a string s consisting of only lowercase English letters. In one operation, you can:
# Delete the entire string s, or
# Delete the first i letters of s if the first i letters of s are equal to the following i letters in s, for any i in the range 1 <= i <= s.length / 2.
# For example, if s = "ababc", then in one operation, you could delete the first two letters of s to get "abc", since the first two letters of s and the following two letters of s are both equal to "ab".
# Return the maximum number of operations needed to delete all of s.
class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s) + 1
        g = [[0] * (n) for _ in range(n)]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    g[i][j] = g[i + 1][j + 1] + 1
        f = [1] * len(s)
        for i in range(len(s) - 1, -1, -1):
            for j in range(1, (len(s) - i) // 2 + 1):
                if g[i][i + j] >= j:
                    f[i] = max(f[i], f[i + j] + 1)
        return f[0]
