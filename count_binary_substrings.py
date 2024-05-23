# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0
        target = s[0]
        prev_num = 0
        cur_num = 0
        res = 0
        for j in range(len(s)):
            if s[j] == target:
                cur_num += 1
            else:
                res += min(prev_num, cur_num)
                prev_num = cur_num
                cur_num = 1
                target = s[j]
        return res + min(prev_num, cur_num)
