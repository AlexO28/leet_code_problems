# You are given two integers n and maxValue, which are used to describe an ideal array.
# A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:
# Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
# Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
# Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        c = [[0] * 16 for _ in range(n)]
        MOD = 1000000007
        maxPlus = maxValue + 1
        for i in range(n):
            for j in range(min(16, i + 1)):
                c[i][j] = 1 if j == 0 else (c[i - 1][j] + c[i - 1][j - 1]) % MOD
        f = [[0] * 16 for _ in range(maxPlus)]
        for i in range(1, maxPlus):
            f[i][1] = 1
        for j in range(1, 15):
            for i in range(1, maxPlus):
                k = 2
                while k * i <= maxValue:
                    f[k * i][j + 1] = (f[k * i][j + 1] + f[i][j]) % MOD
                    k += 1
        res = 0
        for i in range(1, maxPlus):
            for j in range(1, 16):
                res = (res + f[i][j] * c[-1][j - 1]) % MOD
        return res
