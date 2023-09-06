# You are given a string s. You can convert s to a palindromeby adding characters in front of it.
# Return the shortest palindrome you can find by performing this transformation.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if (len(s) == 0) or (len(s) == 1):
            return s
        s_list = list(s)
        if s_list == s_list[::-1]:
            return s
        for j in range(1, len(s)):
            if s_list[:(len(s)-j)] == (s_list[:(len(s)-j)])[::-1]:
                return ''.join(s_list[len(s)-j:][::-1] + s_list)
