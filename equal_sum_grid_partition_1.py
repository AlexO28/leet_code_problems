# You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:
# Each of the two resulting sections formed by the cut is non-empty.
# The sum of the elements in both sections is equal.
# Return true if such a partition exists; otherwise return false.
from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        if len(grid) > 1:
            prefixes = []
            for i in range(len(grid)):
                summa = 0
                for j in range(len(grid[0])):
                    summa += grid[i][j]
                prefixes.append(summa)
            summa_2 = sum(prefixes)
            summa_1 = 0
            for x in range(len(grid) - 1):
                summa_1 += prefixes[x]
                summa_2 -= prefixes[x]
                if summa_1 == summa_2:
                    return True
        if len(grid[0]) > 1:
            prefixes = []
            for j in range(len(grid[0])):
                summa = 0
                for i in range(len(grid)):
                    summa += grid[i][j]
                prefixes.append(summa)
            summa_2 = sum(prefixes)
            summa_1 = 0
            for x in range(len(grid[0]) - 1):
                summa_1 += prefixes[x]
                summa_2 -= prefixes[x]
                if summa_1 == summa_2:
                    return True
        return False
