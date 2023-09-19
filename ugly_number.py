# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 5 == 0:
                n = int(n/5)
            elif n % 3 == 0:
                n = int(n/3)
            elif n % 2 == 0:
                n = int(n/2)
            else:
                return False
        return True
        
