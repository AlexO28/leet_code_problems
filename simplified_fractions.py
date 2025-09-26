# Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. You can return the answer in any order.
from typing import List
from math import gcd


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []
        res = []
        for den in range(2, n + 1):
            for num in range(1, den):
                cur_gcd = gcd(num, den)
                res.append(str(int(num / cur_gcd)) + "/" + str(int(den / cur_gcd)))
        return list(set(res))
