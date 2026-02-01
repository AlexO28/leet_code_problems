# You are given four integers, m, n, introvertsCount, and extrovertsCount. You have an m x n grid, and there are two types of people: introverts and extroverts. There are introvertsCount introverts and extrovertsCount extroverts.
# You should decide how many people you want to live in the grid and assign each of them one grid cell. Note that you do not have to have all the people living in the grid.
# The happiness of each person is calculated as follows:
# Introverts start with 120 happiness and lose 30 happiness for each neighbor (introvert or extrovert).
# Extroverts start with 40 happiness and gain 20 happiness for each neighbor (introvert or extrovert).
# Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.
# The grid happiness is the sum of each person's happiness. Return the maximum possible grid happiness.
from functools import cache


class Solution:
    def getMaxGridHappiness(
        self, m: int, n: int, introvertsCount: int, extrovertsCount: int
    ) -> int:
        self.p = 3 ** (n - 1)
        self.h = [[0, 0, 0], [0, -60, -10], [0, -10, 40]]
        self.square = m * n
        self.n = n
        return self.search(0, 0, introvertsCount, extrovertsCount)

    @cache
    def search(self, pos, pre, ic, ec):
        if pos == self.square or (ic == 0 and ec == 0):
            return 0
        ans = 0
        up = pre // self.p
        if pos % self.n == 0:
            left = 0
        else:
            left = pre % 3
        for i in range(3):
            if (i == 1 and ic == 0) or (i == 2 and ec == 0):
                continue
            cur = pre % self.p * 3 + i
            a = self.h[up][i] + self.h[left][i]
            b = self.search(pos + 1, cur, ic - (i == 1), ec - (i == 2))
            c = 0
            if i == 1:
                c = 120
            elif i == 2:
                c = 40
            ans = max(ans, a + b + c)
        return ans
