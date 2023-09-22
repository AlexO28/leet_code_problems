# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if (len(s) == 0) and (len(t) == 0):
            return True
        if len(t) == 0:
            return False
        pos_1 = 0
        pos_2 = 0
        while True:
            if (pos_1 >= len(t)) and (pos_2 < len(s)):
                return False
            if (pos_2 >= len(s)):
                return True
            if t[pos_1] == s[pos_2]:
                pos_1 += 1
                pos_2 += 1
            else:
                pos_1 += 1
        
