# Given an array of digits digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer return an empty string.
# Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.
from typing import List
from math import inf


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort()
        dp = [[-inf for i in range(3)] for j in range(len(digits) + 1)]
        dp[0][0] = 0
        for i, digit in enumerate(digits, 1):
            for remainder in range(3):
                dp[i][remainder] = max(
                    dp[i - 1][remainder], dp[i - 1][(remainder - digit % 3 + 3) % 3] + 1
                )
        if dp[len(digits)][0] <= 0:
            return ""
        subsequence = []
        remainder = 0
        for i in range(len(digits), 0, -1):
            next_remainder = (remainder - digits[i - 1] % 3 + 3) % 3
            if dp[i - 1][next_remainder] + 1 == dp[i][remainder]:
                subsequence.append(digits[i - 1])
                remainder = next_remainder
        leading_zeros_removed = 0
        while (leading_zeros_removed < len(subsequence) - 1) and (
            subsequence[leading_zeros_removed] == 0
        ):
            leading_zeros_removed += 1
        return "".join(map(str, subsequence[leading_zeros_removed:]))
