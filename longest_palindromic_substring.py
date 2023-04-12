# Given a string s, return the longest palindromic substring in s.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        max_len = 1
        init_pos = 0
        for i in range(len(s)-1):
            temp_len = 1
            for j in range(len(s)-1, i+max_len-1, -1):
                substr = s[i:(j+1)]
                rev_substr = substr[::-1]
                if substr == rev_substr:
                    temp_len = max(temp_len, len(substr))
            if temp_len > max_len:
                init_pos = i
                max_len = temp_len
        return s[init_pos:(init_pos+max_len)]
 
