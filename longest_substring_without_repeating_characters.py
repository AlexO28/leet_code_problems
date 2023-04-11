# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_len = 1
        for i in range(len(s)-1):
            string_dict = {}
            string_dict[s[i]] = 1
            temp_len = 1
            for j in range(i+1, len(s)):
                if s[j] in string_dict.keys():
                    break
                else:
                    temp_len += 1
                    string_dict[s[j]] = 1
            if temp_len > max_len:
                max_len = temp_len
        return max_len
