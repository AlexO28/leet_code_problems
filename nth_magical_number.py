# A positive integer is magical if it is divisible by either a or b.
# Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.
from math import lcm
from bisect import bisect_left


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        return bisect_left(range((a + b) * n), n, key=lambda x: x // a + x // b - x // lcm(a, b)) % (10**9 + 7)
