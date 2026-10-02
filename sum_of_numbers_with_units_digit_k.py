# Given two integers num and k, consider a set of positive integers with the following properties:
# The units digit of each integer is k.
# The sum of the integers is num.
# Return the minimum possible size of such a set, or -1 if no such set exists.
# Note:
# The set can contain multiple instances of the same integer, and the sum of an empty set is considered 0.
# The units digit of a number is the rightmost digit of the number.
from math import inf
from functools import cache


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if (num == 0):
            return 0
        self.numbers = []
        self.k = k
        for j in range(1, num + 1):
            if j % 10 == k:
                self.numbers.append(j)
        res = self.resolve(num)
        return res if res < inf else -1

    @cache
    def resolve(self, x):
        if (x % 10 == self.k):
            return 1
        else:
            candidates = []
            for number in self.numbers:
                if number > x:
                    break
                else:
                    candidates.append(1 + self.resolve(x - number))
            if len(candidates) == 0:
                return inf
            else:
                return min(candidates)
