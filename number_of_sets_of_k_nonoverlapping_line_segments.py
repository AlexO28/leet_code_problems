# Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.
# Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 1000000007
        f = [[0] * (k + 1) for i in range(n + 1)]
        g = [[0] * (k + 1) for j in range(n + 1)]
        f[1][0] = 1
        for i in range(2, n + 1):
            for j in range(k + 1):
                f[i][j] = (f[i - 1][j] + g[i - 1][j]) % MOD
                g[i][j] = g[i - 1][j]
                if j:
                    g[i][j] += f[i - 1][j - 1]
                    g[i][j] %= MOD
                    g[i][j] += g[i - 1][j - 1]
                    g[i][j] %= MOD
        return (f[-1][-1] + g[-1][-1]) % MOD
