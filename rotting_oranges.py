# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        number_of_fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append([i, j])
                elif grid[i][j] == 1:
                    number_of_fresh += 1
        minutes = 0
        if number_of_fresh == 0:
            return minutes
        while len(rotten) > 0:
            minutes += 1
            new_rotten = []
            for i, j in rotten:
                if i > 0:
                    if grid[i-1][j] == 1:
                        new_rotten.append([i-1, j])
                        number_of_fresh -= 1
                        grid[i-1][j] = 2
                if i < len(grid)-1:
                    if grid[i+1][j] == 1:
                        new_rotten.append([i+1, j])
                        number_of_fresh -= 1
                        grid[i+1][j] = 2
                if j > 0:
                    if grid[i][j-1] == 1:
                        new_rotten.append([i, j-1])
                        number_of_fresh -= 1
                        grid[i][j-1] = 2
                if j < len(grid[0])-1:
                    if grid[i][j+1] == 1:
                        new_rotten.append([i, j+1])
                        number_of_fresh -= 1
                        grid[i][j+1] = 2
                if number_of_fresh == 0:
                    return minutes
            rotten = new_rotten.copy()
        return -1
