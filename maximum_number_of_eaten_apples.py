# There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.
# You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.
# Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.
from typing import List
from heapq import heappush, heappop


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        i = 0
        ans = 0
        q = []
        while (i < len(days)) or q:
            if (i < len(days)) and (apples[i] > 0):
                heappush(q, (i + days[i] - 1, apples[i]))
            while q and q[0][0] < i:
                heappop(q)
            if q:
                t, v = heappop(q)
                v -= 1
                ans += 1
                if v and t > i:
                    heappush(q, (t, v))
            i += 1
        return ans
