# Given an integer n, return the number of trailing zeroes in n!.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        number_of_fives = 0
        while n >= 5:
            n //= 5
            number_of_fives += n
        return number_of_fives
