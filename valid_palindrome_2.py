# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if (len(s) < 3):
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (s[left:right] == s[left:right][::-1]) or (s[left+1:right+1] == s[left+1:right+1][::-1])
            left += 1
            right -= 1
        return True
