# We define the string base to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so base will look like this:
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# Given a string s, return the number of unique non-empty substrings of s are present in base.
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        max_length_info = {el:0 for el in 'abcdefghijklmnopqrstuvwxyz'}
        cur_length = 0
        for j in range(len(s)):
            if (j > 0) and ((ord(s[j]) - ord(s[j-1])) % 26 == 1):
                cur_length += 1
            else:
                cur_length = 1
            max_length_info[s[j]] = max(max_length_info[s[j]], cur_length)
        return sum(list(max_length_info.values()))
