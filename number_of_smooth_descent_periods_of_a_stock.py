# You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.
# A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.
# Return the number of smooth descent periods.
from typing import List
from functools import cache


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 1
        res = 0
        i = 0
        while i < len(prices):
            j = i + 1
            while j < len(prices) and prices[j - 1] - prices[j] == 1:
                j += 1
            res += self.estimate(j - i)
            i = j
        return int(res)


    def estimate(self, n):
        return n * (n + 1) / 2
