# You are given an array of n strings strs, all of the same length.
# We may choose any deletion indices, and we delete all the characters in those indices for each string.
# Suppose we chose a set of deletion indices answer such that after deletions, the final array has every string (row) in lexicographic order. (i.e., (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]), and (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]), and so on). Return the minimum possible value of answer.length.
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs[0]) == 1:
            return 0      
        dp = [1] * len(strs[0])
        for i in range(1, len(strs[0])):
            for j in range(i):
                found = False
                for s in strs:
                    if s[j] > s[i]:
                        found = True
                        break
                if not found:
                    dp[i] = max(dp[i], dp[j] + 1)
        return len(strs[0]) - max(dp)
