# Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:
# Append the character '0' zero times.
# Append the character '1' one times.
# This can be performed any number of times.
# A good string is a string constructed by the above process having a length between low and high (inclusive).
# Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        f = [0] * (high + 1)
        for i in range(high, -1, -1):
            res = int(low <= i <= high)
            if i + zero <= high:
                res += f[i + zero]
            if i + one <= high:
                res += f[i + one]
            f[i] = res % 1000000007
        return f[0]
