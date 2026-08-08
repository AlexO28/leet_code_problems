# An original string, consisting of lowercase English letters, can be encoded by the following steps:
# Arbitrarily split it into a sequence of some number of non-empty substrings.
# Arbitrarily choose some elements (possibly none) of the sequence, and replace each with its length (as a numeric string).
# Concatenate the sequence as the encoded string.
# Given two encoded strings s1 and s2, consisting of lowercase English letters and digits 1-9 (inclusive), return true if there exists an original string that could be encoded as both s1 and s2. Otherwise, return false.
# Note: The test cases are generated such that the number of consecutive digits in s1 and s2 does not exceed 3.
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        dp = [[set() for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        dp[0][0].add(0)
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                for delta in tuple(dp[i][j]):
                    num = 0
                    if delta <= 0:
                        for p in range(i, min(i + 3, len(s1))):
                            if s1[p] in "0123456789":
                                num = 10 * num + int(s1[p])
                                dp[p + 1][j].add(delta + num)
                            else:
                                break
                    num = 0
                    if delta >= 0:
                        for q in range(j, min(j + 3, len(s2))):
                            if s2[q] in "0123456789":
                                num = 10 * num + int(s2[q])
                                dp[i][q + 1].add(delta - num)
                            else:
                                break
                    if (i < len(s1)) and (delta < 0) and (s1[i] not in "0123456789"):
                        dp[i + 1][j].add(delta + 1)
                    if (j < len(s2)) and (delta > 0) and (s2[j] not in "0123456789"):
                        dp[i][j + 1].add(delta - 1)
                    if (
                        (i < len(s1))
                        and (j < len(s2))
                        and (delta == 0)
                        and (s1[i] == s2[j])
                    ):
                        dp[i + 1][j + 1].add(0)
        return 0 in dp[-1][-1]
