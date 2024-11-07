# You are given an array of n strings strs, all of the same length.
# The strings can be arranged such that there is one on each line, making a grid.
# For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
# abc
# bce
# cae
# You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
# Return the number of columns that you will delete.
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i in range(len(strs[0])):
            line = []
            for j in range(len(strs)):
                line.append(strs[j][i])
            line_sorted = line.copy()
            line_sorted.sort()
            if line_sorted != line:
                res += 1 
        return res
