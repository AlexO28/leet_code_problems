# Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 1000000007
        ans = 0
        shift = 0
        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                shift += 1
            ans = (ans << shift | i) % MOD
        return ans
