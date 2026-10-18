# We call a positive integer special if all of its digits are distinct
# Given a positive integer n, return the number of special integers that belong to the interval [1, n].
from functools import cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        self.s = str(n)
        return self.search(0, 0, True, True)

    @cache
    def search(self, i, mask, lead, limit):
        if i >= len(self.s):
            return int(lead ^ 1)
        up = int(self.s[i]) if limit else 9
        res = 0
        for j in range(up + 1):
            if not (mask >> j & 1):
                if lead and j == 0:
                    res += self.search(i + 1, mask, True, limit and j == up)
                else:
                    res += self.search(i + 1, mask | 1 << j, False, limit and j == up)
        return res
