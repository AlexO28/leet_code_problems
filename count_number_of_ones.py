# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.


class Solution:
    def countDigitOne(self, n: int) -> int:
        m = 1
        ones = 0
        while m <= n:
            r = int(n / m) % 10
            if r > 1:
                ones += m
            elif r == 1:
                ones += n % m + 1
            ones += int(n / (m * 10)) * m
            m *= 10
        return ones
