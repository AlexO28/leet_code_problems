# Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1
        while k:
            count = self.count_prefix(current, n)
            if k >= count:
                k -= count
                current += 1
            else:
                k -= 1
                current *= 10
        return current

    def count_prefix(self, prefix, n):
        next_prefix = prefix + 1
        total = 0
        while prefix <= n:
            total += min(n - prefix + 1, next_prefix - prefix)
            next_prefix *= 10
            prefix *= 10
        return total
