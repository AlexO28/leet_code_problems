# You are given a string s that consists of the digits '1' to '9' and two integers k and minLength.
# A partition of s is called beautiful if:
# s is partitioned into k non-intersecting substrings.
# Each substring has a length of at least minLength.
# Each substring starts with a prime digit and ends with a non-prime digit. Prime digits are '2', '3', '5', and '7', and the rest of the digits are non-prime.
# Return the number of beautiful partitions of s. Since the answer may be very large, return it modulo 109 + 7.
# A substring is a contiguous sequence of characters within a string.
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        primes = "2357"
        if s[0] not in primes or s[-1] in primes:
            return 0
        n = len(s) + 1
        f = [[0] * (k + 1) for _ in range(n)]
        g = [[0] * (k + 1) for _ in range(n)]
        f[0][0] = 1
        g[0][0] = 1
        for i, c in enumerate(s, 1):
            if i >= minLength and c not in primes and (i == len(s) or s[i] in primes):
                for j in range(1, k + 1):
                    f[i][j] = g[i - minLength][j - 1]
            for j in range(k + 1):
                g[i][j] = (g[i - 1][j] + f[i][j]) % 1000000007
        return f[len(s)][k]
