# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

class Solution:
    def minCut(self, s: str) -> int:
        if len(s) == 1:
            return 0

        pal = [[False for i in range(0, len(s))] for j in range(0, len(s))]

        for i in range(0, len(s)):
            for j in range(0, i + 1):
                pal[j][i] = (s[j] == s[i]) and ((j + 1 > i - 1) or (pal[j + 1][i - 1]))
        
        min_cut = [i for i in range(len(s))]

        for i in range(len(s)):
            for j in range(i+1):
                if pal[j][i]:
                    if j > 0:
                        min_cut[i] = min(min_cut[i], min_cut[j - 1] + 1)
                    else:
                        min_cut[i] = 0

        return min_cut[-1]
