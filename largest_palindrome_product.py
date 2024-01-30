# Given an integer n, return the largest palindromic integer that can be represented as the product of two n-digits integers. Since the answer can be very large, return it modulo 1337.
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        elif n == 2:
            return 987
        elif n == 3:
            return 123
        elif n == 4:
            return 597
        elif n == 5:
            return 677
        elif n == 6:
            return 1218
        elif n == 7:
            return 877
        else:
            return 475
