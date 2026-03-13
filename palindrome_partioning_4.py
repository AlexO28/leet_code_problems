# Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​
# A string is said to be palindrome if it the same string when reversed.
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        f = [[True] * len(s) for i in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                f[i][j] = (s[i] == s[j]) and ((i + 1 == j) or f[i + 1][j - 1])
        for i in range(len(s) - 2):
            for j in range(i + 1, len(s) - 1):
                if f[0][i] and f[i + 1][j] and f[j + 1][-1]:
                    return True
        return False
