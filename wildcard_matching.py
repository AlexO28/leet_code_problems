# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '':
            if s == '':
                return True
            else:
                return False
        elif s == '':
            if p.strip('*') == '':
                return True
            else: 
                return False
        dp = [[False for i in range(0, max(len(s), len(p)) + 5)]
                     for j in range(0, max(len(s), len(p)) + 5)]
        if p[0] == '*':
            for i in range(0, len(s) + 1):
                dp[1][i] = True
        elif p[0] == '?':
            dp[1][1] = True
        else:
            dp[1][1] = (p[0] == s[0])
        
        for i in range(1, len(p)):
            if p[i] == '*':
                for j in range(0, len(s) + 1):
                    if dp[i][j] == True:
                        for k in range(j - 1, len(s)):
                            dp[i + 1][k + 1] = True
            elif p[i] == '?':
                for j in range(0, len(s)):
                    dp[i + 1][j + 1] = dp[i][j]
            else:
                for j in range(0, len(s)):
                    dp[i + 1][j + 1] = (dp[i][j]) and (p[i] == s[j])         
        return dp[len(p)][len(s)]
