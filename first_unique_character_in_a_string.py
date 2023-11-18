# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = {}
        for elem in s:
            if elem in s_dict.keys():
                s_dict[elem] = 2
            else:
                s_dict[elem] = 1
        for j in range(len(s)):
            if s_dict[s[j]] == 1:
                return j
        return -1
  
