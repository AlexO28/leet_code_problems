# An ugly number is a positive integer that is divisible by a, b, or c.
# Given four integers n, a, b, and c, return the nth ugly number.
from math import lcm


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab_lcm = lcm(a, b)
        bc_lcm = lcm(b, c)
        ac_lcm = lcm(a, c)
        abc_lcm = lcm(a, b, c)
        left = 1
        right = 2 * 10 ** 9
        while left < right:
            mid = (left + right) // 2
            count = mid // a + mid // b + mid // c - mid // ab_lcm - mid // bc_lcm - mid // ac_lcm + mid // abc_lcm
            if count >= n:
                right = mid
            else:
                left = mid + 1
        return left
