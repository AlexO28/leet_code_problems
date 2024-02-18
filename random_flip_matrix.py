# There is an m x n binary grid matrix with all the values set 0 initially. Design an algorithm to randomly pick an index (i, j) where matrix[i][j] == 0 and flips it to 1. All the indices (i, j) where matrix[i][j] == 0 should be equally likely to be returned.
# Optimize your algorithm to minimize the number of calls made to the built-in random function of your language and optimize the time and space complexity.
# Implement the Solution class:
# Solution(int m, int n) Initializes the object with the size of the binary matrix m and n.
# int[] flip() Returns a random index [i, j] of the matrix where matrix[i][j] == 0 and flips it to 1.
# void reset() Resets all the values of the matrix to be 0.

import random

class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.map = {}
        self.len = m*n
        self.len_pure = self.len

    def flip(self) -> List[int]:
        self.len -= 1
        x = randint(0, self.len)
        idx = self.map.get(x, x)
        self.map[x] = self.map.get(self.len, self.len)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.len = self.len_pure
        self.map.clear()
