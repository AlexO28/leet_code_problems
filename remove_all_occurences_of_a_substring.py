# Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
# Find the leftmost occurrence of the substring part and remove it from s.
# Return s after removing all occurrences of part.
# A substring is a contiguous sequence of characters in a string.
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if len(part) > len(s):
            return s
        res = []
        for j in range(len(s)):
            res.append(s[j])
            if len(res) >= len(part):
                if "".join(res[(len(res)-len(part)):len(res)]) == part:
                    res = res[:(len(res)-len(part))]
        return "".join(res)
