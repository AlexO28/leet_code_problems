# You are given an integer array nums. We call a subset of nums good if its product can be represented as a product of one or more distinct prime numbers.
# Return the number of different good subsets in nums modulo 109 + 7.
# A subset of nums is any array that can be obtained by deleting some (possibly none or all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.
from collections import Counter
from typing import List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cnt = Counter(nums)
        MOD = 1000000007
        NUMBER_OF_SUBSETS = 1024
        f = [0] * 1024
        f[0] = pow(2, cnt[1])
        for x in range(2, 31):
            if (cnt[x] == 0) or (x % 4 == 0) or (x % 9 == 0) or (x % 25 == 0):
                continue
            mask = 0
            for i, p in enumerate(PRIMES):
                if x % p == 0:
                    mask |= 1 << i
            for state in range(1023, 0, -1):
                if state & mask == mask:
                    f[state] = (f[state] + cnt[x] * f[state ^ mask]) % MOD
        return sum(f[i] for i in range(1, 1024)) % MOD
