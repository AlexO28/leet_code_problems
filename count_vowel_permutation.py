# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:=
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.
import numpy as np


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        transition_matrix = np.matrix(
            [
                [0, 1, 0, 0, 0],
                [1, 0, 1, 0, 0],
                [1, 1, 0, 1, 1],
                [0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0],
            ]
        )
        res = np.matrix([1, 1, 1, 1, 1])
        n -= 1
        while n > 0:
            if n & 1:
                res = (res * transition_matrix) % MOD
            transition_matrix = (transition_matrix * transition_matrix) % MOD
            n >>= 1
        return int(res.sum() % MOD)
