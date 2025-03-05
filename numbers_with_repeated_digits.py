# Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.
from functools import cache


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        return n - self._countSpecialNumbers(n)

    def _countSpecialNumbers(self, n):
        self.s = str(n)
        return self._search(0, 0, True) - 1

    @cache
    def _search(self, i, used, isTight):
        if i == len(self.s):
            return 1
        res = 0
        if isTight:
            maxDigit = int(self.s[i])
        else:
            maxDigit = 9
        for d in range(maxDigit + 1):
            if used >> d & 1:
                continue
            nextIsTight = isTight and (d == maxDigit)
            if used == 0 and d == 0:  # Don't count leading 0s as used.
                res += self._search(i + 1, used, nextIsTight)
            else:
                res += self._search(i + 1, used | 1 << d, nextIsTight)
        return res
