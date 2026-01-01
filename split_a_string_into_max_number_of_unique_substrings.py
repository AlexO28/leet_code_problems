# Given a string s, return the maximum number of unique substrings that the given string can be split into.
# You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
# A substring is a contiguous sequence of characters within a string.
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.d = {}
        return self.calculateSplit(s)

    def calculateSplit(self, s):
        maxm = 0
        for i in range(1, len(s) + 1):
            tmp = s[0:i]
            if tmp not in self.d:
                self.d[tmp] = 1
                maxm = max(maxm, self.calculateSplit(s[i:]) + 1)
                del self.d[tmp]
        return maxm
