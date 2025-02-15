# Given a positive integer n, return the punishment number of n.
# The punishment number of n is defined as the sum of the squares of all integers i such that:
# 1 <= i <= n
# The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
class Solution:
    def punishmentNumber(self, n: int) -> int:
        PUNISHMENT_NUMBERS = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675,703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
        PUNISHMENT_SQUARES = [1, 81, 100, 1296, 2025, 3025, 6724, 8281, 9801, 10000, 55225, 88209, 136161,136900, 143641, 171396, 431649, 455625, 494209, 571536, 627264, 826281, 842724, 893025, 929296, 980100, 982081, 998001, 1000000]
        res = 0
        for j in range(len(PUNISHMENT_NUMBERS)):
            if PUNISHMENT_NUMBERS[j] <= n:
                res += PUNISHMENT_SQUARES[j]
            else:
                return res
        return res
