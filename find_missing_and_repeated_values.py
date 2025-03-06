# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n2 = len(grid) ** 2
        num_dict = {i: 1 for i in range(1, n2 + 1)}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in num_dict:
                    del num_dict[grid[i][j]]
                else:
                    a = grid[i][j]
        b = list(num_dict.keys())[0]
        return [a, b]
