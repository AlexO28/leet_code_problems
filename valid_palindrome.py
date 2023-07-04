# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [symb.lower() for symb in s if symb.isalnum()]
        if len(s) == 0:
            return True
        return s == s[::-1]
