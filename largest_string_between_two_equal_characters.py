# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
# A substring is a contiguous sequence of characters within a string.
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_dict = {}
        res = -1
        for j in range(len(s)):
            if s[j] in char_dict.keys():
                res = max(res, j-char_dict[s[j]]-1)
            else:
                char_dict[s[j]] = j
        return res
