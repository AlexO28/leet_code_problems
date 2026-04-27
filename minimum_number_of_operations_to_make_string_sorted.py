# You are given a string s (0-indexed)​​​​​​. You are asked to perform the following operation on s​​​​​​ until you get a sorted string:
# Find the largest index i such that 1 <= i < s.length and s[i] < s[i - 1].
# Find the largest index j such that i <= j < s.length and s[k] < s[i - 1] for all the possible values of k in the range [i, j] inclusive.
# Swap the two characters at indices i - 1​​​​ and j​​​​​.
# Reverse the suffix starting at index i​​​​​​.
# Return the number of operations needed to make the string sorted. Since the answer can be too large, return it modulo 109 + 7.
from collections import Counter


class Solution:
    def makeStringSorted(self, s: str) -> int:
        N = len(s)
        MOD = 1000000007
        f = [1] + [0] * N
        g = f.copy()
        for i in range(1, N):
            f[i] = f[i - 1] * i % MOD
            g[i] = pow(f[i], MOD - 2, MOD)
        cnt = Counter(s)
        ans = 0
        for i, c in enumerate(s):
            m = sum(v for a, v in cnt.items() if a < c)
            t = f[len(s) - i - 1] * m
            for v in cnt.values():
                t = t * g[v] % MOD
            ans = (ans + t) % MOD
            cnt[c] -= 1
            if cnt[c] == 0:
                cnt.pop(c)
        return ans
