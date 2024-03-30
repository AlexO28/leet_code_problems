# Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.
from functools import cache


class Solution:
    def findIntegers(self, n: int) -> int:
        self.binary_representation = [0] * 33
        length = 0
        while n:
            length += 1
            self.binary_representation[length] = n & 1
            n >>= 1
        return self.dfs(length, 0, True)

    @cache
    def dfs(self, position, previous_digit, is_limited):
        if position <= 0:
            return 1
        if is_limited:
            upper_bound = self.binary_representation[position]
        else: 
            upper_bound = 1
        count = 0
        for digit in range(upper_bound + 1): 
            if previous_digit == 1 and digit == 1:
                continue
            count += self.dfs(position - 1, digit, is_limited and digit == upper_bound)
        return count
