# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
# Return the score of s.
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for j in range(len(s)-1):
            res += abs(ord(s[j+1]) - ord(s[j]))
        return res
