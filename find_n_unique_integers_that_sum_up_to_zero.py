# Given an integer n, return any array containing n unique integers such that they add up to 0.
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        main_part, remainder = divmod(n, 2)
        res = []
        for j in range(1, main_part + 1):
            res.append(j)
            res.append(-j)
        if remainder > 0:
            res.append(0)
        return res
