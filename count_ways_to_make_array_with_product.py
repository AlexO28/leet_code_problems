# You are given a 2D integer array, queries. For each queries[i], where queries[i] = [ni, ki], find the number of different ways you can place positive integers into an array of size ni such that the product of the integers is ki. As the number of ways may be too large, the answer to the ith query is the number of ways modulo 109 + 7.
# Return an integer array answer where answer.length == queries.length, and answer[i] is the answer to the ith query.
from typing import List
from collections import defaultdict
from math import comb


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        self.MOD = 1000000007
        N = 10020
        self.f = [1] * N
        self.g = [1] * N
        p = defaultdict(list)
        for i in range(1, N):
            self.f[i] = self.f[i - 1] * i % self.MOD
            self.g[i] = pow(self.f[i], self.MOD - 2, self.MOD)
            x = i
            j = 2
            while j <= x // j:
                if x % j == 0:
                    cnt = 0
                    while x % j == 0:
                        cnt += 1
                        x //= j
                    p[i].append(cnt)
                j += 1
            if x > 1:
                p[i].append(1)
        ans = []
        for n, k in queries:
            t = 1
            for x in p[k]:
                t = t * self.comb(x + n - 1, n - 1) % self.MOD
            ans.append(t)
        return ans

    def comb(self, n, k):
        return self.f[n] * self.g[k] * self.g[n - k] % self.MOD
