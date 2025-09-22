# Given the strings s1 and s2 of size n and the string evil, return the number of good strings.
# A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 109 + 7.
from functools import cache


class Solution:
    def findGoodStrings(self, n, s1, s2, evil):
        self.MOD = 10**9 + 7
        self.m = len(evil)
        self.n = n
        self.s1 = s1
        self.s2 = s2
        self.evil = evil
        self.fail = [0] * self.m
        for i in range(1, self.m):
            j = self.fail[i - 1]
            while j > 0 and evil[i] != evil[j]:
                j = self.fail[j - 1]
            if evil[i] == evil[j]:
                j += 1
            self.fail[i] = j
        return self.search(0, 0, True, True)

    @cache
    def search(self, pos, matched, tight_low, tight_high):
        if matched == self.m:
            return 0
        if pos == self.n:
            return 1
        res = 0
        if tight_low:
            low = self.s1[pos]
        else:
            low = "a"
        if tight_high:
            high = self.s2[pos]
        else:
            high = "z"
        for c in range(ord(low), ord(high) + 1):
            ch = chr(c)
            k = matched
            while k > 0 and self.evil[k] != ch:
                k = self.fail[k - 1]
            if self.evil[k] == ch:
                k += 1
            res += self.search(
                pos + 1, k, tight_low and ch == low, tight_high and ch == high
            )
            res %= self.MOD
        return res
