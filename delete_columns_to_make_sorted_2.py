# You are given an array of n strings strs, all of the same length.
# We may choose any deletion indices, and we delete all the characters in those indices for each string.
# For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].
# Suppose we chose a set of deletion indices answer such that after deletions, the final array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum possible value of answer.length.
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs) == 1:
            return 0
        deletions = 0
        sorted_status = [False]*(len(strs))
        for j in range(len(strs[0])):
            found = False
            for i in range(len(strs)-1):
                if not sorted_status[i] and strs[i][j] > strs[i+1][j]:
                    deletions += 1
                    found = True
                    break
            if not found:
                for i in range(len(strs)-1):
                    if strs[i][j] < strs[i+1][j]:
                        sorted_status[i] = True
        return deletions
