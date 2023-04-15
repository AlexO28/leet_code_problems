# Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x = str(x)
        x_reverted = x[::-1]
        return x == x_reverted
