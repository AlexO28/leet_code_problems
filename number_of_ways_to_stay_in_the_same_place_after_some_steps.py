# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).
# Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.
from functools import cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        self.mod = 10**9 + 7
        return self.search(0, steps, arrLen)

    @cache
    def search(self, current_index, remaining_steps, arrLen):
        if (
            current_index > remaining_steps
            or current_index >= arrLen
            or current_index < 0
            or remaining_steps < 0
        ):
            return 0
        if current_index == 0 and remaining_steps == 0:
            return 1
        number_of_ways = 0
        for move in range(-1, 2):
            number_of_ways += self.search(current_index + move, remaining_steps - 1, arrLen)
            number_of_ways %= self.mod
        return number_of_ways
