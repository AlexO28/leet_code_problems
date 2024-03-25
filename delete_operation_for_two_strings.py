# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp_table = [[0] * (len(word2) + 1) for j in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            dp_table[i][0] = i
        for j in range(1, len(word2) + 1):
            dp_table[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1]
                else:
                    dp_table[i][j] = 1 + min(dp_table[i - 1][j], dp_table[i][j - 1])
        return dp_table[-1][-1]
