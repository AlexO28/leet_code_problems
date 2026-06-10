# You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.
# Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.
from collections import defaultdict


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 1000000007
        maxVal = 3**m
        valid = {i for i in range(maxVal) if self.f1(i, m)}
        d = defaultdict(list)
        for x in valid:
            for y in valid:
                if self.f2(x, y, m):
                    d[x].append(y)
        f = [int(i in valid) for i in range(maxVal)]
        for _ in range(n - 1):
            g = [0] * maxVal
            for i in valid:
                for j in d[i]:
                    g[i] = (g[i] + f[j]) % MOD
            f = g
        return sum(f) % MOD

    def f1(self, x, m):
        last = -1
        for _ in range(m):
            main_part_x, remainder_x = divmod(x, 3)
            if remainder_x == last:
                return False
            last = remainder_x
            x = main_part_x
        return True

    def f2(self, x, y, m):
        for _ in range(m):
            main_part_x, remainder_x = divmod(x, 3)
            main_part_y, remainder_y = divmod(y, 3)
            if remainder_x == remainder_y:
                return False
            x = main_part_x
            y = main_part_y
        return True
